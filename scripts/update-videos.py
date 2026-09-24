from __future__ import annotations

import json
import os
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

CHANNEL_ID = "UCcjZE3dOZkpSHp4wqSRTorw"
FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "videos.json"
ATOM = "{http://www.w3.org/2005/Atom}"
MEDIA = "{http://search.yahoo.com/mrss/}"
YT = "{http://www.youtube.com/xml/schemas/2015}"


def fetch_videos() -> list[dict[str, str]]:
    request = urllib.request.Request(
        FEED_URL,
        headers={"User-Agent": "Nesaganam-YouTube-Feed/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        root = ET.fromstring(response.read())

    videos = []
    for entry in root.findall(f"{ATOM}entry"):
        video_id = entry.findtext(f"{YT}videoId")
        title = entry.findtext(f"{ATOM}title")
        published = entry.findtext(f"{ATOM}published")
        alternate_link = entry.find("{http://www.w3.org/2005/Atom}link[@rel='alternate']")
        video_url = alternate_link.get("href", "") if alternate_link is not None else ""
        if video_id and title:
            videos.append(
                {
                    "id": video_id,
                    "title": title,
                    "published": published or "",
                    "type": "short" if "/shorts/" in video_url else "video",
                }
            )
    return videos


def main() -> None:
    fetched_videos = fetch_videos()
    if not fetched_videos:
        raise RuntimeError("The YouTube feed returned no videos.")

    existing_videos = []
    if OUTPUT_PATH.exists():
        existing_videos = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))

    videos_by_id = {video["id"]: video for video in existing_videos if video.get("id")}
    videos_by_id.update({video["id"]: video for video in fetched_videos})
    videos = sorted(
        videos_by_id.values(),
        key=lambda video: video.get("published", ""),
        reverse=True,
    )

    OUTPUT_PATH.write_text(
        json.dumps(videos, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(videos)} videos to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
