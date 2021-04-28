const fetch=require('node-fetch')
const fs = require('fs')

const getImage = async(i) => {

  const response = await fetch("https://thispersondoesnotexist.com/image", {
    credentials: "include",
    headers: {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "image/webp,*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Sec-GPC": "1",
        "If-Modified-Since": "Wed, 18 Nov 2020 13:11:19 GMT",
        "If-None-Match": "\"5fb51d77-724d7\"",
        "Cache-Control": "max-age=0"
    },
    referrer: "https://thispersondoesnotexist.com/",
    method: "GET",
    mode: "cors"
  })
  const buffer = await response.buffer();
  fs.writeFile(`./images/${i}.jpeg`, buffer, () => 
  console.log('finished downloading!'));
  return i
}

let loop = async() => {
  for(let i = 1; i < 10000; i++){
    let test = await getImage(i)
    console.log(test)
  }  
}

loop()

