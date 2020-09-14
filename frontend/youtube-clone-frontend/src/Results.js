import React, { Component, useEffect, useState } from "react";
import { FormProvider } from "react-hook-form";
import InfiniteScroll from 'react-infinite-scroll-component';

const Results = (props) => {

    const [items, setItems] = useState([]);

    function fetchMoreData() {

      fetch("/search?start=0&num=12", {
      })
      .then(response => response.json())
      .then(data => {
          setItems(items.concat(data['data']))
      })
    }

    useEffect(() => {
      const urlParams = new URLSearchParams(props.location.search);
      fetch("/search?start=0&num=12&q=" + urlParams.get('q'), {
      })
      .then(response => response.json())
      .then(data => {
          setItems(data['data']);
          console.log(data);
      })
    }, [props.location]);
  
    return (
      <div class="search-results">
        RESULTS
        <div class="results-list">
          <InfiniteScroll
            dataLength={items.length}
            next={fetchMoreData}
            hasMore={true}
            scrollableTarget="videos-container"
            loader={<h4>Loading...</h4>}>
                {items.map((val) => (
                    <VideoItem 
                        title={val.title} 
                        view_count={val.view_count} 
                        upload_date={val.upload_date}
                        video_length={val.video_length}
                        static_url={val.static_url}
                        animated_url={val.animated_url}
                        channel={val.channel}
                        video_url={val.video_url}
                    />
                ))}
            </InfiniteScroll>
        </div>
      </div>
    )
}

function VideoItem(props) {
  return (
    <div class="result-video-item">
      {props.title}
    </div>
  )
}

export default Results;
