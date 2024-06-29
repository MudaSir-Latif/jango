class Participant {
    constructor(name, photography_url) {
      this.setName(name);
      this.photography_url = photography_url;
    }

    getName() {
      return this.name;
    }

    setName(newName) {
      newName = newName.trim();
      if (newName === '') {
        throw 'The name cannot be empty';
      }
      this.name = newName;
    }

    getPhotography() {
      return this.photography_url;
    }
  }

  let participant1 = new Participant("Polina Ajit", "img/people/4.png");
  let participant2 = new Participant("Dezső Rashmi", "img/people/5.png");
  let participant3 = new Participant("Lore Adrian", "img/people/6.png");
  let participant4 = new Participant("Patrick Asim", "img/people/7.png");
  let participant5 = new Participant("Neha Patka", "img/people/8.png");

  let participants = new Map([
    [participant1, 303],
    [participant2, 322],
    [participant3, 144],
    [participant4, 297],
    [participant5, 192]
  ]);

  participants[Symbol.iterator] = function* () {
    yield* [...this.entries()].sort((a, b) => b[1] - a[1]);
  }

  let bronze = [...participants][2];
  let silver = [...participants][1];
  let gold = [...participants][0];


  let silverChampionImg = document.getElementById("silver_profile");
  let goldChampionImg = document.getElementById("gold_profile");
  let bronzeChampionImg = document.getElementById("bronze_profile");

  let silverChampionName = document.getElementById("silver_profile_name");
  let goldChampionName = document.getElementById("gold_profile_name");
  let bronzeChampionName = document.getElementById("bronze_profile_name");

  let silverChampionPoint = document.getElementById("silver_profile_point");
  let goldChampionPoint = document.getElementById("gold_profile_doint");
  let bronzeChampionPoint = document.getElementById("bronze_profile_point");

  silverChampionImg.src =  silver[0].getPhotography();
  goldChampionImg.src =  gold[0].getPhotography();
  bronzeChampionImg.src =  bronze[0].getPhotography();

  silverChampionName.innerHTML = silver[0].getName();
  goldChampionName.innerHTML = gold[0].getName();
  bronzeChampionName.innerHTML =  bronze[0].getName();

  silverChampionPoint.innerHTML = silver[1];
  goldChampionPoint.innerHTML =  gold[1];
  bronzeChampionPoint.innerHTML =  bronze[1];




