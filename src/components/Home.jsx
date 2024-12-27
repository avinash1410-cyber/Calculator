import React, { useState } from 'react';

function Home() {
  const [num1, setNum1] = useState('');
  const [num2, setNum2] = useState('');
  const [result, setResult] = useState(null);

  // Function to perform the selected operation
  async function calculate(operation) {
    const n1 = parseFloat(num1);
    const n2 = parseFloat(num2);
    
    if (isNaN(n1) || isNaN(n2)) {
      setResult('Please enter valid numbers');
      return;
    }

    try {
      let response;
      let data;

      if (operation === "add") {
        response = await fetch(`http://127.0.0.1:8000/add/?a=${n1}&b=${n2}`);
      } else if (operation === "subtract") {
        response = await fetch(`http://127.0.0.1:8000/subtract/?a=${n1}&b=${n2}`);
      } else if (operation === "multiply") {
        response = await fetch(`http://127.0.0.1:8000/multiply/?a=${n1}&b=${n2}`);
      } else if (operation === "divide") {
        response = await fetch(`http://127.0.0.1:8000/divide/?a=${n1}&b=${n2}`);
      }

      data = await response.json();
      setResult(data.result); // Assuming the API returns a result key

    } catch (error) {
      setResult('Error fetching data');
    }
  }

  return (
    <div className="flex flex-col items-center p-4">
      <h1 className="text-xl font-bold mb-4">Simple Calculator</h1>
      
      {/* Input fields for numbers */}
      <div className="mb-4">
        <input
          type="number"
          value={num1}
          onChange={(e) => setNum1(e.target.value)}
          className="border p-2 mr-2"
          placeholder="First number"
        />
        <input
          type="number"
          value={num2}
          onChange={(e) => setNum2(e.target.value)}
          className="border p-2"
          placeholder="Second number"
        />
      </div>

      {/* Buttons for each operation */}
      <div className="mb-4">
        <button className="px-4 py-2 mx-2 border" onClick={() => calculate("add")}>
          Add
        </button>
        <button className="px-4 py-2 mx-2 border" onClick={() => calculate("subtract")}>
          Subtract
        </button>
        <button className="px-4 py-2 mx-2 border" onClick={() => calculate("multiply")}>
          Multiply
        </button>
        <button className="px-4 py-2 mx-2 border" onClick={() => calculate("divide")}>
          Divide
        </button>
      </div>

      {/* Display result */}
      <div className="mt-4">
        {result !== null && (
          <p className="text-lg font-semibold">Result: {result}</p>
        )}
      </div>
    </div>
  );
}

export default Home;
