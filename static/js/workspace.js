var instructionArray = [];
var historyInstruct = [];
var storexml ="";
var workspace = Blockly.inject('blocklyDiv', {
  toolbox: document.getElementById('toolbox'),
  trashcan: true,
  scrollbars: true
});

function clearworkspace() {
 workspace.clear();
 instructionArray.splice(0, instructionArray.length);
 historyInstruct.splice(0, historyInstruct.length);
 console.log("Coding environment cleared")
}
function saveToXML() {
    var xmlDom = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
    var xmlText = Blockly.Xml.domToPrettyText(xmlDom);
    storexml = xmlText;
    console.log(storexml);
}

function xmlToWorkspace() {
    var xml = Blockly.Xml.textToDom(storexml);
    Blockly.Xml.domToWorkspace(xml, workspace);
}

function move_forward() {
    let value = 1
    instructionArray.push(value)
    historyInstruct.push("Move Forward")
}

function turn_right() {
    let value = 2
    instructionArray.push(value)
    historyInstruct.push("Turn Right")
}

function turn_left() {
    let value = 3
    instructionArray.push(value)
    historyInstruct.push("Turn Left")
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
                save(historyInstruct);
                saveToXML();
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
            let ans2 = [1,3,1,2,1,3,1,2,1,3,1,2,1,3,1,2,1];
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
    if (old_data.length > 3){
        old_data.shift();
    }
    //Save old + new data
    localStorage.setItem('instructionHistory', JSON.stringify(old_data));
    
    //Counting number of items in instructionHistory
    var noItems = JSON.parse(localStorage.instructionHistory).length;
    
    //Save them for displaying
    if (noItems === 1){
        localStorage.setItem('firstrow', JSON.stringify(old_data[0]));
    }
    if (noItems === 2){
        localStorage.setItem('firstrow', JSON.stringify(old_data[0]));
        localStorage.setItem('secondrow', JSON.stringify(old_data[1]));
    }
    if (noItems === 3){
        localStorage.setItem('firstrow', JSON.stringify(old_data[0]));
        localStorage.setItem('secondrow', JSON.stringify(old_data[1]));
        localStorage.setItem('thirdrow', JSON.stringify(old_data[2]));
    }
    viewPast();
}
function viewPast(){
    if(localStorage.getItem('firstrow') != null){
        var checkArray1 = JSON.parse(localStorage.getItem('firstrow'));
        let datetime1 = checkArray1[checkArray1.length - 1];
        checkArray1.pop();
        document.getElementById('firstRow').innerHTML = datetime1 + " - " + checkArray1.join(" > ");
        if(localStorage.getItem('secondrow') != null){
            var checkArray2 = JSON.parse(localStorage.getItem('secondrow'));
            let datetime2 = checkArray2[checkArray2.length - 1];
            checkArray2.pop();
            document.getElementById('secondRow').innerHTML = datetime2 + " - " + checkArray2.join(" > ");
            if(localStorage.getItem('thirdrow') != null){
                var checkArray3 = JSON.parse(localStorage.getItem('thirdrow'));
                let datetime3 = checkArray3[checkArray3.length - 1];
                checkArray3.pop();
                document.getElementById('thirdRow').innerHTML = datetime3 + " - " + checkArray3.join(" > ");
            }
        }
    }
}