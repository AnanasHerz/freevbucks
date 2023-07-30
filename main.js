const loadVideo = meta => {
    fetch('https://api.rss2json.com/v1/api.json?rss_url=https://www.youtube.com/feeds/videos.xml?channel_id=UCEWIYszywEy8TK4xgfrQbPA')
    .then(response => response.json())
    .then(result => {
        console.log(result)
        let index = 0
        var link = result.items[index].link
        var title = result.items[index].title
        console.log(link)
        while (title.includes('#shorts')) {
            index++
            link = result.items[index].link
            title = result.items[index].title
            console.log(link)
        }
        const meta = document.querySelector("meta")
        meta.setAttribute('content', `0; url=${link}`)
    })
    .catch(error => console.log('error', error))
}
loadVideo()