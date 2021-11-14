var workspace = Blockly.inject('blocklyDiv', {
  toolbox: document.getElementById('toolbox'),
  trashcan: true,
  scrollbars: true
});

function clearworkspace() {
 workspace.clear();
 console.log("Coding environment cleared")
}
function move_forward() {
    let x = "go forward";
    console.log(x);
}

function turn_right() {
    let x = "go right";
    console.log(x);
}

function turn_left() {
    let x = "go left";
    console.log(x);
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
    } catch (e) {
        alert(e);
    }
}