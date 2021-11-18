const instructionArray = [];
var workspace = Blockly.inject('blocklyDiv', {
  toolbox: document.getElementById('toolbox'),
  trashcan: true,
  scrollbars: true
});

function clearworkspace() {
 workspace.clear();
 instructionArray.splice(0, instructionArray.length);
 console.log("Coding environment cleared")
}
function move_forward() {
    let value = 1
    instructionArray.push(value)
}

function turn_right() {
    let value = 2
    instructionArray.push(value)
}

function turn_left() {
    let value = 3
    instructionArray.push(value)
}

function runCode() {
    // Generate JavaScript code and run it.
    window.LoopTrap = 1000;
    Blockly.JavaScript.INFINITE_LOOP_TRAP =
        'if (--window.LoopTrap == 0) throw "Infinite loop.";\n';
    var code = Blockly.JavaScript.workspaceToCode(workspace);
    Blockly.JavaScript.INFINITE_LOOP_TRAP = null;
    try {
        //execute the argument which is a function
        eval(code);
        console.log(instructionArray);
        pathname = window.location.pathname;
        console.log(pathname);
        switch (pathname){
            case "/challenge1.html":
                check_answer(1);
                break;
            case "/challenge2.html":
                check_answer(2);
                break;
            case "/challenge3.html":
                check_answer(3);
                break;
            default:
                save(instructionArray);
                console.log("Dashboard");
        }
    } catch (e) {
        alert(e);
    }
    clearworkspace();
}

function check_answer(num) {
    switch (num){
        case 1:
            let ans1 = [1,3,1,2,1];
            if (arrayEquals(instructionArray,ans1)) {
                console.log("Challenge 1 complete");
                $('#completedModal').modal('show');
            }
            else {
                console.log("Answer wrong!!");
                $('#wrongModal').modal('show');
            }
            break;
        case 2:
            let ans2 = [1,2,1,3,1,2,1,3,1,2,1,3,1,2,1,3];
            if (arrayEquals(instructionArray,ans2)) {
                console.log("Challenge 2 complete");
                 $('#completedModal').modal('show');
            }
            else {
                console.log("Answer wrong!!");
                $('#wrongModal').modal('show');
            }
            break;
        case 3:
            let ans3 = [1,1,3,1,1,3,1,2,1,1,2,1,1,3,1];
            if (arrayEquals(instructionArray,ans3)) {
                console.log("Challenge 3 complete");
                $('#completedModal').modal('show');
            }
            else {
                console.log("Answer wrong!!");
                $('#wrongModal').modal('show');
            }
            break;
        default:
            console.log("Something is Wrong !!!");
    }
}

function arrayEquals(a, b) {
    return Array.isArray(a) &&
        Array.isArray(b) &&
        a.length === b.length &&
        a.every((val, index) => val === b[index]);
}

function save(data){
    var today = new Date();
    var date = ((today.getDate() < 10)?"0":"") + today.getDate() +"/"+(((today.getMonth()+1) < 10)?"0":"") + (today.getMonth()+1) +"/"+ today.getFullYear();
    var time = ((today.getHours() < 10)?"0":"") + today.getHours() +":"+ ((today.getMinutes() < 10)?"0":"") + today.getMinutes() +":"+ ((today.getSeconds() < 10)?"0":"") + today.getSeconds();
    var dateTime = date+' '+time;
    data.push(dateTime);
    
    //LocalStorage with variable instructionHistory
    if(localStorage.getItem('instructionHistory') == null){
        localStorage.setItem('instructionHistory', '[]');
    }
    //Fetch old data
    var old_data = JSON.parse(localStorage.getItem('instructionHistory'));
    
    //Append push new data
    old_data.push(data);
    if (old_data.length > 5){
        old_data.shift();
    }
    
    //Save old + new data
    localStorage.setItem('instructionHistory', JSON.stringify(old_data));
}