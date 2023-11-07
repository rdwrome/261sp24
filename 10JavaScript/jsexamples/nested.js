var name = 'Wendy'; // global
function cheep() {
  var greeting = 'Howdy'; // in 'cheep()'
  {
    let encourg = 'Go'; // in 'console.log()'
    console.log(`${encourg}: ${greeting} ${name}`);
  }
} // in 'cheep()'
//
cheep();
