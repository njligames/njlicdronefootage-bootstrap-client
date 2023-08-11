
#!/usr/local/bin/python3

import sys
import csv

# video_url="https://player.vimeo.com/video/447948883?badge=0&autoplay=1&loop=1"
# button_img="assets/img/gallery/services7.png"
# button_text="Aerial Marketing Video: Weaving Stories, Uniting Perspectives"

item="""
<div class="col-lg-4">
  <div class="single-cat">
    <div class="cat-icon">
      <div class="cat-icon">
        <button
          type="button"
          class="video-btn"
          data-toggle="modal"
          data-src="{video_url}"
          data-target="#myModal"
        >
          <img
            class="video-btn-img"
            src="{button_img}"
            alt=""
          />
        </button>
      </div>
    </div>
    <div class="cat-cap">
      <h5>
        <a href="#pricing">
        {button_text}
        </a>
      </h5>
    </div>
  </div>
</div>
"""

if(len(sys.argv) > 1):
    # filename="tickets_test.csv"
    # filename="residential_real_estate.csv"
    filename = sys.argv[1]

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        output=""
        for row in reader:
            output += item.format(video_url=row["video_url"], button_img=row["button_img"], button_text=row["button_text"])

        print(output)
