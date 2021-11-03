//==================================================== MOVEMENT ====================================================
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
  var code = '...;\n';
  return code;
};
