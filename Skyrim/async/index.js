function creatures()  {

     fetch("creatures.json")
      .then(response => response.json())
      .then(modules => {
      let output = "";
      modules.forEach(module => {
            output += "<p>Creature: " + module.name + ", Description: " + module.description + "</p>";
      });
    document.getElementById("result").innerHTML = output;
}); 

}

function places()  {

     fetch("places.json")
      .then(response => response.json())
      .then(modules => {
      let output = "";
      modules.forEach(module => {
            output += "<p>Name: " + module.name + ", leader: " + module.leader + "</p>";
      });
    document.getElementById("result").innerHTML = output;
}); 

}


