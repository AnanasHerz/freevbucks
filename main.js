const loadVideo = (meta) => {
    const reqURL = `https://api.rss2json.com/v1/api.json?rss_url=https://www.youtube.com/feeds/videos.xml?channel_id=UCEWIYszywEy8TK4xgfrQbPA`;

    fetch(reqURL)
        .then(response => response.json())
        .then(result => {
          console.log(result)
            const link = result.items[0].link;
            console.log(link)
            meta[0].setAttribute("content", `0; url=${link}`);
        })
        .catch(error => console.log('error', error));
}
const meta = document.getElementsByClassName('redirect');
loadVideo(meta);