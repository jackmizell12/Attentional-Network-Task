/************ 
 * Ant Test *
 ************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1, 1, 1]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'ANT';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instrRoutineBegin());
flowScheduler.add(instrRoutineEachFrame());
flowScheduler.add(instrRoutineEnd());
flowScheduler.add(instr2RoutineBegin());
flowScheduler.add(instr2RoutineEachFrame());
flowScheduler.add(instr2RoutineEnd());
flowScheduler.add(instr3RoutineBegin());
flowScheduler.add(instr3RoutineEachFrame());
flowScheduler.add(instr3RoutineEnd());
flowScheduler.add(instr4RoutineBegin());
flowScheduler.add(instr4RoutineEachFrame());
flowScheduler.add(instr4RoutineEnd());
flowScheduler.add(practice_instrRoutineBegin());
flowScheduler.add(practice_instrRoutineEachFrame());
flowScheduler.add(practice_instrRoutineEnd());
const practiceLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoopBegin, practiceLoopScheduler);
flowScheduler.add(practiceLoopScheduler);
flowScheduler.add(practiceLoopEnd);
flowScheduler.add(trial_instrRoutineBegin());
flowScheduler.add(trial_instrRoutineEachFrame());
flowScheduler.add(trial_instrRoutineEnd());
flowScheduler.add(MainTrialInstructRoutineBegin());
flowScheduler.add(MainTrialInstructRoutineEachFrame());
flowScheduler.add(MainTrialInstructRoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin, trials_3LoopScheduler);
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instrClock;
var instr_1;
var key_resp;
var image;
var instr2Clock;
var instr_2;
var key_resp_2;
var image_2_1;
var image_2_2;
var instr3Clock;
var text;
var key_resp_3;
var image_3;
var instr4Clock;
var instr_4;
var key_resp_4;
var image_4;
var practice_instrClock;
var pract_instr;
var key_resp_5;
var pract_trialClock;
var fix_1;
var pract_warning;
var fix_2;
var pract_target;
var pract_resp;
var feedback_2Clock;
var msg;
var text_3;
var trial_instrClock;
var practice_res;
var key_resp_6;
var MainTrialInstructClock;
var text_5;
var key_resp_7;
var trialClock;
var fixation_1;
var warning;
var fixation_2;
var target;
var post_fixation;
var response;
var break_2Clock;
var break_message;
var break_key;
var endClock;
var text_2;
var end_key;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  instr_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_1',
    text: 'This is a task investigating attention.\n\nYou will be shown an arrow on the screen pointing to either the \nleft or the right.\n\nOn some trials, the arrow will be flanked by\ntwo arrows to the left or two arrows to the \nright. They may or may not point in the same direction as the \nCENTER arrow.\n\n\n\n\n\n\n\n\nYour task is to respond to the direction of the CENTER arrow.\n\n\n\nPress the SPACEBAR to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'ANT_images/image1.png', mask : undefined,
    ori : 0, pos : [0, (- 0.1)], size : [0.5, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "instr2"
  instr2Clock = new util.Clock();
  instr_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_2',
    text: "left: 'E' key                                            right: 'I' key\n\nPress the left response button ('E') if the CENTER arrow \npoints to the left.\n\n\n\n\n\nPress the right reponse arrow ('I') if the CENTER arrow \npoints to the right.\n\n\n\n\n\nPlease make your reponse as quickly and accurately as \npossible. Your reaction time and accuracy will be recorded.\n\n\n\nPress the SPACEBAR to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_2_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2_1', units : undefined, 
    image : 'ANT_images/image2.1.png', mask : undefined,
    ori : 0, pos : [0, 0.14], size : [0.5, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  image_2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2_2', units : undefined, 
    image : 'ANT_images/image2.2.png', mask : undefined,
    ori : 0, pos : [0, (- 0.1)], size : [0.5, 0.12],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "instr3"
  instr3Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'There will be a cross in the center of the screen \nand the arrows will appear either above or below the cross.\n\nYou should try to fixate on the cross throughout the task.\n\n\n\nPress the SPACEBAR to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : 'ANT_images/image3.png', mask : undefined,
    ori : 0, pos : [0, (- 0.07)], size : [0.7, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "instr4"
  instr4Clock = new util.Clock();
  instr_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_4',
    text: 'Additionally, on some trials there will be a black star \nflashed onto the screen shortly before the arrows appear.\n\nThese stars indicate where the arrow will occur:\n\n\n\n\n\n\n\n\n\nIf the star is at the center or both above and below fixation \nit indicates both that the trial will occur shortly and WHERE \nit will occur.\n\nTry to maintain fixation at all times. However, you may attend \nwhen and where indicated by the cues.\n\n\n\nPress the SPACEBAR to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : 'ANT_images/image4.png', mask : undefined,
    ori : 0, pos : [0, 0.1], size : [0.6, 0.15],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "practice_instr"
  practice_instrClock = new util.Clock();
  pract_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'pract_instr',
    text: "This task contains four blocks:\n\nThe first block is for practice only and takes about two minutes. After each \nblock there will be a message 'take a break' and you may take a short rest.\n\nThe whole session takes about twenty minutes.\n\n\n\nPress the SPACEBAR to start PRACTICE",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pract_trial"
  pract_trialClock = new util.Clock();
  fix_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  pract_warning = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pract_warning', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  fix_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fix_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  pract_target = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pract_target', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.7, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  pract_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback_2"
  feedback_2Clock = new util.Clock();
  msg = "";
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "trial_instr"
  trial_instrClock = new util.Clock();
  practice_res = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_res',
    text: '\nYou have completed the practice trials.\n\n\n\n  Press SPACEBAR to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "MainTrialInstruct"
  MainTrialInstructClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'Now the actual task can be started.\n\nThere will be three blocks. Each block takes about\nfive minutes. Totally, you just need to spend 15 minutes.\n\n\n\n   Press the SPACEBAR to start the task \n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  fixation_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixation_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  warning = new visual.ImageStim({
    win : psychoJS.window,
    name : 'warning', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  fixation_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixation_2', units : undefined, 
    image : 'ANT_images/fixation.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  target = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.7, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  post_fixation = new visual.ImageStim({
    win : psychoJS.window,
    name : 'post_fixation', units : undefined, 
    image : 'ANT_images/fixation.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "break_2"
  break_2Clock = new util.Clock();
  break_message = new visual.TextStim({
    win: psychoJS.window,
    name: 'break_message',
    text: 'You have reached the end of this trial. You may take a short break before continuing.\n\nPlease press the SPACEBAR when you are ready to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  break_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  fixation_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixation_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  warning = new visual.ImageStim({
    win : psychoJS.window,
    name : 'warning', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  fixation_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixation_2', units : undefined, 
    image : 'ANT_images/fixation.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  target = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.7, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  post_fixation = new visual.ImageStim({
    win : psychoJS.window,
    name : 'post_fixation', units : undefined, 
    image : 'ANT_images/fixation.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'You have completed the test.\n\nThank you for participating.\n\nPress the SPACEBAR to save your data and finish.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  end_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _key_resp_allKeys;
var instrComponents;
function instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr'-------
    t = 0;
    instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    instrComponents = [];
    instrComponents.push(instr_1);
    instrComponents.push(key_resp);
    instrComponents.push(image);
    
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_1* updates
    if (t >= 0 && instr_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_1.tStart = t;  // (not accounting for frame time here)
      instr_1.frameNStart = frameN;  // exact frame index
      
      instr_1.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr'-------
    instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var instr2Components;
function instr2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr2'-------
    t = 0;
    instr2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    instr2Components = [];
    instr2Components.push(instr_2);
    instr2Components.push(key_resp_2);
    instr2Components.push(image_2_1);
    instr2Components.push(image_2_2);
    
    instr2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_2* updates
    if (t >= 0.0 && instr_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_2.tStart = t;  // (not accounting for frame time here)
      instr_2.frameNStart = frameN;  // exact frame index
      
      instr_2.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image_2_1* updates
    if (t >= 0.0 && image_2_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2_1.tStart = t;  // (not accounting for frame time here)
      image_2_1.frameNStart = frameN;  // exact frame index
      
      image_2_1.setAutoDraw(true);
    }

    
    // *image_2_2* updates
    if (t >= 0.0 && image_2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2_2.tStart = t;  // (not accounting for frame time here)
      image_2_2.frameNStart = frameN;  // exact frame index
      
      image_2_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr2'-------
    instr2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var instr3Components;
function instr3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr3'-------
    t = 0;
    instr3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    instr3Components = [];
    instr3Components.push(text);
    instr3Components.push(key_resp_3);
    instr3Components.push(image_3);
    
    instr3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image_3* updates
    if (t >= 0.0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index
      
      image_3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr3'-------
    instr3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instr3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var instr4Components;
function instr4RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr4'-------
    t = 0;
    instr4Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    instr4Components = [];
    instr4Components.push(instr_4);
    instr4Components.push(key_resp_4);
    instr4Components.push(image_4);
    
    instr4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr4RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr4'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr_4* updates
    if (t >= 0.0 && instr_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_4.tStart = t;  // (not accounting for frame time here)
      instr_4.frameNStart = frameN;  // exact frame index
      
      instr_4.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image_4* updates
    if (t >= 0.0 && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index
      
      image_4.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr4RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr4'-------
    instr4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instr4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var practice_instrComponents;
function practice_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'practice_instr'-------
    t = 0;
    practice_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    practice_instrComponents = [];
    practice_instrComponents.push(pract_instr);
    practice_instrComponents.push(key_resp_5);
    
    practice_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function practice_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'practice_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = practice_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pract_instr* updates
    if (t >= 0.0 && pract_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pract_instr.tStart = t;  // (not accounting for frame time here)
      pract_instr.frameNStart = frameN;  // exact frame index
      
      pract_instr.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'practice_instr'-------
    practice_instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "practice_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var practice;
var currentLoop;
function practiceLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  practice = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'ANT_practice.xlsx',
    seed: undefined, name: 'practice'
  });
  psychoJS.experiment.addLoop(practice); // add the loop to the experiment
  currentLoop = practice;  // we're now the current loop

  // Schedule all the trials in the trialList:
  practice.forEach(function() {
    const snapshot = practice.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(pract_trialRoutineBegin(snapshot));
    thisScheduler.add(pract_trialRoutineEachFrame(snapshot));
    thisScheduler.add(pract_trialRoutineEnd(snapshot));
    thisScheduler.add(feedback_2RoutineBegin(snapshot));
    thisScheduler.add(feedback_2RoutineEachFrame(snapshot));
    thisScheduler.add(feedback_2RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function practiceLoopEnd() {
  psychoJS.experiment.removeLoop(practice);

  return Scheduler.Event.NEXT;
}


var trials_2;
function trials_2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_2'
  });
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_2.forEach(function() {
    const snapshot = trials_2.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    thisScheduler.add(trialsLoopScheduler);
    thisScheduler.add(trialsLoopEnd);
    thisScheduler.add(break_2RoutineBegin(snapshot));
    thisScheduler.add(break_2RoutineEachFrame(snapshot));
    thisScheduler.add(break_2RoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'ANT_conditions.xlsx',
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trialRoutineBegin(snapshot));
    thisScheduler.add(trialRoutineEachFrame(snapshot));
    thisScheduler.add(trialRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


var trials_3;
function trials_3LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'ANT_conditions.xlsx',
    seed: undefined, name: 'trials_3'
  });
  psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
  currentLoop = trials_3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_3.forEach(function() {
    const snapshot = trials_3.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trialRoutineBegin(snapshot));
    thisScheduler.add(trialRoutineEachFrame(snapshot));
    thisScheduler.add(trialRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}


var _pract_resp_allKeys;
var pract_trialComponents;
function pract_trialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'pract_trial'-------
    t = 0;
    pract_trialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    fix_1.setImage('ANT_images/fixation.png');
    pract_warning.setImage(cue_file);
    fix_2.setImage('ANT_images/fixation.png');
    pract_target.setPos([0, pos]);
    pract_target.setImage(flanker);
    pract_resp.keys = undefined;
    pract_resp.rt = undefined;
    _pract_resp_allKeys = [];
    // keep track of which components have finished
    pract_trialComponents = [];
    pract_trialComponents.push(fix_1);
    pract_trialComponents.push(pract_warning);
    pract_trialComponents.push(fix_2);
    pract_trialComponents.push(pract_target);
    pract_trialComponents.push(pract_resp);
    
    pract_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function pract_trialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'pract_trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = pract_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix_1* updates
    if (t >= 0.0 && fix_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_1.tStart = t;  // (not accounting for frame time here)
      fix_1.frameNStart = frameN;  // exact frame index
      
      fix_1.setAutoDraw(true);
    }

    frameRemains = 0.0 + fix1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix_1.setAutoDraw(false);
    }
    
    // *pract_warning* updates
    if (t >= fix1 && pract_warning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pract_warning.tStart = t;  // (not accounting for frame time here)
      pract_warning.frameNStart = frameN;  // exact frame index
      
      pract_warning.setAutoDraw(true);
    }

    frameRemains = fix1 + cue_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pract_warning.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pract_warning.setAutoDraw(false);
    }
    
    // *fix_2* updates
    if (((pract_warning.status == FINISHED)) && fix_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_2.tStart = t;  // (not accounting for frame time here)
      fix_2.frameNStart = frameN;  // exact frame index
      
      fix_2.setAutoDraw(true);
    }

    if (fix_2.status === PsychoJS.Status.STARTED && t >= (fix_2.tStart + 0.4)) {
      fix_2.setAutoDraw(false);
    }
    
    // *pract_target* updates
    if (((fix_2.status == FINISHED)) && pract_target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pract_target.tStart = t;  // (not accounting for frame time here)
      pract_target.frameNStart = frameN;  // exact frame index
      
      pract_target.setAutoDraw(true);
    }

    if (pract_target.status === PsychoJS.Status.STARTED && t >= (pract_target.tStart + 1.7)) {
      pract_target.setAutoDraw(false);
    }
    
    // *pract_resp* updates
    if (t >= stimStart && pract_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pract_resp.tStart = t;  // (not accounting for frame time here)
      pract_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { pract_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { pract_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { pract_resp.clearEvents(); });
    }

    frameRemains = stimStart + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pract_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pract_resp.status = PsychoJS.Status.FINISHED;
  }

    if (pract_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = pract_resp.getKeys({keyList: ['e', 'i'], waitRelease: false});
      _pract_resp_allKeys = _pract_resp_allKeys.concat(theseKeys);
      if (_pract_resp_allKeys.length > 0) {
        pract_resp.keys = _pract_resp_allKeys[_pract_resp_allKeys.length - 1].name;  // just the last key pressed
        pract_resp.rt = _pract_resp_allKeys[_pract_resp_allKeys.length - 1].rt;
        // was this correct?
        if (pract_resp.keys == correct) {
            pract_resp.corr = 1;
        } else {
            pract_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    pract_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pract_trialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'pract_trial'-------
    pract_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (pract_resp.keys === undefined) {
      if (['None','none',undefined].includes(correct)) {
         pract_resp.corr = 1;  // correct non-response
      } else {
         pract_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('pract_resp.keys', pract_resp.keys);
    psychoJS.experiment.addData('pract_resp.corr', pract_resp.corr);
    if (typeof pract_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('pract_resp.rt', pract_resp.rt);
        routineTimer.reset();
        }
    
    pract_resp.stop();
    // the Routine "pract_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var feedback_2Components;
function feedback_2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'feedback_2'-------
    t = 0;
    feedback_2Clock.reset(); // clock
    frameN = -1;
    routineTimer.add(0.400000);
    // update component parameters for each repeat
    if ((! pract_resp.keys)) {
        msg = "No response";
    } else {
        if (pract_resp.corr) {
            msg = "Correct!";
        } else {
            msg = "Incorrect";
        }
    }
    
    text_3.setColor(new util.Color('black'));
    text_3.setText(msg);
    // keep track of which components have finished
    feedback_2Components = [];
    feedback_2Components.push(text_3);
    
    feedback_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function feedback_2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'feedback_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = feedback_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    frameRemains = 0 + 0.4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    feedback_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedback_2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'feedback_2'-------
    feedback_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_6_allKeys;
var trial_instrComponents;
function trial_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial_instr'-------
    t = 0;
    trial_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    trial_instrComponents = [];
    trial_instrComponents.push(practice_res);
    trial_instrComponents.push(key_resp_6);
    
    trial_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function trial_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trial_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_res* updates
    if (t >= 0.0 && practice_res.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_res.tStart = t;  // (not accounting for frame time here)
      practice_res.frameNStart = frameN;  // exact frame index
      
      practice_res.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial_instr'-------
    trial_instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "trial_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_7_allKeys;
var MainTrialInstructComponents;
function MainTrialInstructRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'MainTrialInstruct'-------
    t = 0;
    MainTrialInstructClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    // keep track of which components have finished
    MainTrialInstructComponents = [];
    MainTrialInstructComponents.push(text_5);
    MainTrialInstructComponents.push(key_resp_7);
    
    MainTrialInstructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function MainTrialInstructRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'MainTrialInstruct'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = MainTrialInstructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    
    // *key_resp_7* updates
    if (t >= 0.0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    MainTrialInstructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MainTrialInstructRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'MainTrialInstruct'-------
    MainTrialInstructComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
    if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
        routineTimer.reset();
        }
    
    key_resp_7.stop();
    // the Routine "MainTrialInstruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _response_allKeys;
var trialComponents;
function trialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    fixation_1.setImage('ANT_images/fixation.png');
    warning.setImage(cue_file);
    target.setPos([0, pos]);
    target.setImage(flanker);
    response.keys = undefined;
    response.rt = undefined;
    _response_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(fixation_1);
    trialComponents.push(warning);
    trialComponents.push(fixation_2);
    trialComponents.push(target);
    trialComponents.push(post_fixation);
    trialComponents.push(response);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function trialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_1* updates
    if (t >= 0 && fixation_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_1.tStart = t;  // (not accounting for frame time here)
      fixation_1.frameNStart = frameN;  // exact frame index
      
      fixation_1.setAutoDraw(true);
    }

    frameRemains = 0 + fix1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_1.setAutoDraw(false);
    }
    
    // *warning* updates
    if (t >= fix1 && warning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      warning.tStart = t;  // (not accounting for frame time here)
      warning.frameNStart = frameN;  // exact frame index
      
      warning.setAutoDraw(true);
    }

    frameRemains = fix1 + cue_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (warning.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      warning.setAutoDraw(false);
    }
    
    // *fixation_2* updates
    if (((warning.status == FINISHED)) && fixation_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_2.tStart = t;  // (not accounting for frame time here)
      fixation_2.frameNStart = frameN;  // exact frame index
      
      fixation_2.setAutoDraw(true);
    }

    if (fixation_2.status === PsychoJS.Status.STARTED && t >= (fixation_2.tStart + 0.4)) {
      fixation_2.setAutoDraw(false);
    }
    
    // *target* updates
    if (((fixation_2.status == FINISHED)) && target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target.tStart = t;  // (not accounting for frame time here)
      target.frameNStart = frameN;  // exact frame index
      
      target.setAutoDraw(true);
    }

    if (target.status === PsychoJS.Status.STARTED && t >= (target.tStart + 1.7)) {
      target.setAutoDraw(false);
    }
    
    // *post_fixation* updates
    if (((target.status == FINISHED)) && post_fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      post_fixation.tStart = t;  // (not accounting for frame time here)
      post_fixation.frameNStart = frameN;  // exact frame index
      
      post_fixation.setAutoDraw(true);
    }

    if (post_fixation.status === PsychoJS.Status.STARTED && t >= (post_fixation.tStart + x)) {
      post_fixation.setAutoDraw(false);
    }
    
    // *response* updates
    if ((stimStart) && response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response.tStart = t;  // (not accounting for frame time here)
      response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { response.clearEvents(); });
    }

    if (response.status === PsychoJS.Status.STARTED && t >= (response.tStart + 1.7)) {
      response.status = PsychoJS.Status.FINISHED;
  }

    if (response.status === PsychoJS.Status.STARTED) {
      let theseKeys = response.getKeys({keyList: ['e', 'i'], waitRelease: false});
      _response_allKeys = _response_allKeys.concat(theseKeys);
      if (_response_allKeys.length > 0) {
        response.keys = _response_allKeys[_response_allKeys.length - 1].name;  // just the last key pressed
        response.rt = _response_allKeys[_response_allKeys.length - 1].rt;
        // was this correct?
        if (response.keys == correct) {
            response.corr = 1;
        } else {
            response.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (response.keys === undefined) {
      if (['None','none',undefined].includes(correct)) {
         response.corr = 1;  // correct non-response
      } else {
         response.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('response.keys', response.keys);
    psychoJS.experiment.addData('response.corr', response.corr);
    if (typeof response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('response.rt', response.rt);
        routineTimer.reset();
        }
    
    response.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _break_key_allKeys;
var break_2Components;
function break_2RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'break_2'-------
    t = 0;
    break_2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    break_key.keys = undefined;
    break_key.rt = undefined;
    _break_key_allKeys = [];
    // keep track of which components have finished
    break_2Components = [];
    break_2Components.push(break_message);
    break_2Components.push(break_key);
    
    break_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function break_2RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'break_2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = break_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *break_message* updates
    if (t >= 0.0 && break_message.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      break_message.tStart = t;  // (not accounting for frame time here)
      break_message.frameNStart = frameN;  // exact frame index
      
      break_message.setAutoDraw(true);
    }

    
    // *break_key* updates
    if (t >= 0.5 && break_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      break_key.tStart = t;  // (not accounting for frame time here)
      break_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { break_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { break_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { break_key.clearEvents(); });
    }

    if (break_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = break_key.getKeys({keyList: ['space'], waitRelease: false});
      _break_key_allKeys = _break_key_allKeys.concat(theseKeys);
      if (_break_key_allKeys.length > 0) {
        break_key.keys = _break_key_allKeys[_break_key_allKeys.length - 1].name;  // just the last key pressed
        break_key.rt = _break_key_allKeys[_break_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    break_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function break_2RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'break_2'-------
    break_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _end_key_allKeys;
var endComponents;
function endRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end'-------
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    end_key.keys = undefined;
    end_key.rt = undefined;
    _end_key_allKeys = [];
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(text_2);
    endComponents.push(end_key);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function endRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *end_key* updates
    if (t >= 0.0 && end_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_key.tStart = t;  // (not accounting for frame time here)
      end_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_key.clearEvents(); });
    }

    if (end_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_key.getKeys({keyList: ['space'], waitRelease: false});
      _end_key_allKeys = _end_key_allKeys.concat(theseKeys);
      if (_end_key_allKeys.length > 0) {
        end_key.keys = _end_key_allKeys[_end_key_allKeys.length - 1].name;  // just the last key pressed
        end_key.rt = _end_key_allKeys[_end_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end'-------
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
