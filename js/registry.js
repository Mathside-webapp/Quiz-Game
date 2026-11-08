// Developer-reviewed modules only. Future engines must provide start, stop and results.
export const games = [
{id:'comic-race',name:'Comic Race',tag:'READY, SET, LEARN',description:'A new adventure is heading for the starting line.',color:'cyan',status:'Coming soon',formats:['multiple-choice'],engine:null},
{id:'castle-siege',name:'Castle Siege',tag:'KNOWLEDGE IS YOUR KINGDOM',description:'A world of castles, courage, and classroom discovery.',color:'purple',status:'Coming soon',formats:['multiple-choice'],engine:null},
{id:'tug-of-war',name:'Tug of War',tag:'BETTER TOGETHER',description:'Big ideas. Shared discoveries. One unforgettable team.',color:'pink',status:'Coming soon',formats:['multiple-choice'],engine:null}
];
export function canLaunch(game,quiz){return !!game?.engine && quiz.questions.length>0 && quiz.questions.every(q=>game.formats.includes(q.type));}
