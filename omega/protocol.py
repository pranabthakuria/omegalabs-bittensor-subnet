# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# Copyright © 2023 Omega Labs, Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import typing
import bittensor as bt
from pydantic import BaseModel


class VideoMetadata(BaseModel):
    """
    A model class representing YouTube video metadata.

    Attributes:
    - id: the YouTube video ID
    - description: a detailed description of the video
    - views: the number of views the video has received
    - likes: the number of likes the video has received
    """
    id: str
    description: str
    views: int
    start_time: int
    end_time: int


class Videos(bt.Synapse):
    """
    A synapse class representing a video scraping request and response.

    Attributes:
    - query: the input query for which to find relevant videos
    - num_videos: the number of videos to return
    - video_metadata: a list of video metadata objects
    """

    query: str
    num_videos: int = 32
    video_metadata: typing.List[VideoMetadata]

    def deserialize(self) -> int:
        return self.video_metadata