const loadVideo = meta => {
    fetch('https://api.rss2json.com/v1/api.json?rss_url=https://www.youtube.com/feeds/videos.xml?channel_id=UCEWIYszywEy8TK4xgfrQbPA')  //YT-API
    .then(response => response.json())
    .then(result => {
        let index = 0
        var link = result.items[index].link             //Link
        var title = result.items[index].title           //Title
        while (title.includes('#shorts')) {             //Checks the title until it doesn't include #shorts
            index++
            link = result.items[index].link
            title = result.items[index].title
        }
        console.log(link)                               //Final Link
        const meta = document.querySelector("meta")
        meta.setAttribute('content', `0; url=${link}`)  //Sets the redirect element to the correct link
    })
    .catch(error => console.log('error', error))
}
loadVideo()