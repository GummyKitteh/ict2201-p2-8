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

function showCode() {
    // Generate JavaScript code and display it.
    Blockly.JavaScript.INFINITE_LOOP_TRAP = null;
    var code = Blockly.JavaScript.workspaceToCode(workspace);
    alert(code);
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
    } catch (e) {
        alert(e);
    }
    clearworkspace();
}
