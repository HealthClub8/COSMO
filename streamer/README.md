# COSMO
COSMO Project Overview

The COSMO project began after my son asked me to build a **robot** for his granddad, who is disabled. In the UK alone, there are over 3 million people with similar conditions, yet the market lacks accessible and effective products to meet their needs. Seeing this gap, we started an open-source project to develop a small, user-friendly robot designed specifically to help my dad.


### Support the project by purchasing my book [COSMO](https://cosmo.yes.app). All proceeds will be donated to charity and individuals in need, like my dad. [COSMO](https://cosmo.yes.app) an audio book — a captivating and original puzzle book inspired by my dad. It's unlike any other book you've read before, blending mystery and emotion with a unique structure that keeps you guessing until the fascinating and unexpected ending.

![Logo](https://cosmo.yes.app/poster_eng.jpg)

Currently, we have integrated a single core service called Streamer, which combines several key technologies:

    1. Chromecast - for streaming content
    2. Raspberry Pi - used as a streamer to Chromecast (though any headless Linux Python executor could be substituted)
    KODI (OpenELEC) - selected to explore potential value from this integration, with the flexibility to replace it with another Linux-based solution or plain vanilla Linux in the future

Since my dad cannot operate a TV on his own, we needed a system that could automatically play video, audio, and online services (like YouTube, Netflix, and Spotify) on a set schedule. Another major issue we encountered was the inability to control content recommendations from platforms like YouTube and Spotify. Their algorithms are designed to maximize engagement, not necessarily to provide meaningful or beneficial content. I've seen this problem with using iPads, the algorithm takes over, feeding them content it thinks is relevant, often leading down a rabbit hole of low-quality or inappropriate material like war, politics, or mindless distractions. 

The same problem arose with my dad. He would watch YouTube on his iPad, but there was no way to filter out content and create a controlled, beneficial viewing experience. Despite trying various solutions like setting limits, marking content as "disliked," and using parental controls it felt like a constant battle against the algorithm rather than a real solution. This highlighted the need for a system where we, as caregivers, could curate content directly, ensuring that only positive, engaging, and beneficial material reaches him.
Together with my son, we realized this setup could go beyond entertainment it could deliver educational programs, learning materials, films, audiobooks, meditation, and relaxation content, improving my dad's mood and cognitive engagement.

To solve this, I created a predefined list of videos and built a simple database of curated content tailored specifically to his needs. This includes:

    bible.txt       -> Bible 
    films.txt       -> Free YouTube films ID's in his native language
    robots.txt      -> As a talented engineer, he loves DIY projects, electronics, robotics, solar tech, and EVs.
    books.txt       -> Free YouTube Audiobooks (also in his native language)
    exercises.txt   -> Guided exercises
    travel.txt      -> Travel videos
    meditation      -> Meditation sessions
    relax.txt       -> Simple nature sounds: rain, ocean etc. 

Technically, I created these playlists of YouTube videos outside of YouTube by compiling a folder-based database (DB) containing the IDs of preselected videos. This way, the content is directly accessible without relying on YouTube's recommendation algorithm. While this setup could eventually evolve into a structured database, for now, I'm following the KISS principle (Keep It Simple, Stupid) maintaining a straightforward, easy-to-manage system that just works.

Currently, the system simply streams a random file from the curated list on a schedule. This approach helps keep things simple and quick to implement. In the future, I plan to add a memory feature that will track which videos have already been played and prioritize unplayed content. This will prevent the same content from appearing twice and ensure a more varied and engaging experience over time. For now, the random approach works well for quick deployment and testing.

Looking ahead, this solution has the potential to serve broader applications beyond personal use. It could be adapted for schools, kids and parent controlled streaming, clubs, restaurants, bars, exhibition centers, libraries, corporate events, receptions, and hotels - essentially any setting where scheduled content delivery could enhance the user experience.

- [Dependencies](#dependencies)
- [Honorable mentions](#honorable-mentions)

# Dependencies

None! this script is written in pure vanilla Python 3+.

# Usage

    python stream.py

# Honorable mentions
 * Anton Hvornum Aka Torxed https://github.com/Torxed/chromecast
 * [Perth Linux User Group](http://plug.org.au/)'s [talk from 2016](https://docs.google.com/presentation/d/1X1BdFunVnLkF7L0BgevH2zzkcSe0_gtdTJ_pMdEuakQ/htmlpresent).
 * [pychromecast](https://github.com/home-assistant-libs/pychromecast) Which had a lot of `URN`'s that could be re-used.
 * [casttube](https://github.com/ur1katz/casttube) Which had all the YouTube Web-API's to manage a YouTube lounge.
 * Google for making the [ProtoBuf](https://developers.google.com/protocol-buffers/docs/encoding) protocol very open and easy to deconstruct.

## Support the project by purchasing my book [COSMO](https://cosmo.yes.app). All proceeds will be donated to charity and individuals in need, like my dad.

![Logo](https://cosmo.yes.app/promotion_eng.jpg)
![Logo](https://cosmo.yes.app/bonus_eng.jpg)

## Support the project by purchasing my book [COSMO](https://cosmo.yes.app). All proceeds will be donated to charity and individuals in need, like my dad.
