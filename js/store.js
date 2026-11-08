const key='quiz-universe-v1';
const question=(prompt,options,answer=0)=>({id:crypto.randomUUID(),type:'multiple-choice',prompt,options,answer});
const seed=[{id:'exponents',title:'Laws of Exponents',subject:'Mathematics',grade:'Grade 8',topic:'Algebra',questions:[question('What is 2³ × 2²?',['2⁵','2⁶','4⁵','4⁶']),question('What is the value of 5⁰?',['1','0','5','10']),question('Simplify x⁶ ÷ x².',['x⁴','x³','x⁸','x¹²'])]},{id:'earth',title:'Our Amazing Earth',subject:'Science',grade:'Grade 7',topic:'Earth science',questions:[question('Which layer is the outermost layer of Earth?',['Crust','Mantle','Outer core','Inner core']),question('Which ocean is the largest?',['Pacific','Atlantic','Indian','Arctic'])]},{id:'linear',title:'Linear Functions',subject:'Mathematics',grade:'Grade 8',topic:'Algebra',questions:[question('In y = 3x + 2, what is the slope?',['3','2','5','1']),question('When x = 2, what is y in y = 2x + 1?',['5','3','4','7'])]}];
export function read(){try {const data=JSON.parse(localStorage.getItem(key)); if(data&&Array.isArray(data.quizzes))return data;}catch{} return {quizzes:seed,results:[],settings:{motion:true,name:'Teacher'}};}
export let state=read();
export function save(){localStorage.setItem(key,JSON.stringify(state));}
export const blankQuestion=()=>question('', ['', '', '', '']);
