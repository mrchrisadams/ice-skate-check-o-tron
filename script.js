// fetch the title of the coloured
// blue is for "geplant, aber noch nicht bestätigt und daher noch nicht buchbar"
// we want either
// = Es gibt noch freie Plätze!
// or Hier gibt es nur noch wenige Plätze! 

const result = document.querySelector("tr.text:nth-child(5) > td:nth-child(9) img").title

let available
if (result === "geplant, aber noch nicht best\u00e4tigt und daher noch nicht buchbar") {
    console.log("still not available")
    available = {"available": false}
} else {
    console.log("ZOMG! Available")
    available = {"status": true}
}

available