

//==================================================== TURN RIGHT ====================================================
Blockly.Blocks['turn_right'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Turn Right");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};
Blockly.JavaScript['turn_right'] = function(block) {
// Assemble JavaScript into code variable.
  var code = 'turn_right();\n';
  return code;
};

//==================================================== TURN LEFT ====================================================
Blockly.Blocks['turn_left'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Turn Left");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};
Blockly.JavaScript['turn_left'] = function(block) {
// Assemble JavaScript into code variable.
  var code = 'turn_left();\n';
  return code;
};

//==================================================== MOVE FORWARD ====================================================
Blockly.Blocks['move_forward'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move Forward");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};
Blockly.JavaScript['move_forward'] = function(block) {
// Assemble JavaScript into code variable.
  var code = 'move_forward();\n';
  return code;
};
