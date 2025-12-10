<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CNN Pooling Visualization</title>
    <!-- Load Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom styles for the matrix cells */
        .grid-cell {
            min-width: 3.5rem; /* Slightly smaller for flexibility */
            min-height: 3.5rem;
            width: auto;
            height: auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.125rem;
            font-weight: 700;
            border: 2px solid #374151; /* Dark Gray Border */
            transition: all 0.3s ease-in-out;
            user-select: none;
            padding: 0.5rem;
        }

        /* Input Feature Map Styling */
        .input-cell {
            background-color: #f3f4f6; /* Light Gray Background */
        }

        /* Active Pooling Kernel (The Window) */
        .active-kernel {
            background-color: #d1fae5; /* Light Green */
            border-color: #10b981; /* Green Border */
            transform: scale(1.05);
            box-shadow: 0 4px 6px -1px rgba(16, 185, 129, 0.4), 0 2px 4px -2px rgba(16, 185, 129, 0.4);
            z-index: 10;
            position: relative;
        }

        /* Highlight the Maximum Value found in the kernel */
        .max-value {
            background-color: #fef3c7; /* Light Yellow */
            border-color: #f59e0b; /* Amber Border */
            transform: scale(1.1);
        }

        /* Output Matrix Styling */
        .output-cell {
            background-color: #bfdbfe; /* Light Blue */
            border-color: #3b82f6; /* Blue Border */
            opacity: 0.5; /* Dim until filled */
        }

        /* Output cell when it receives the Max Value */
        .filled-output {
            opacity: 1;
            background-color: #93c5fd; /* Brighter Blue */
            transform: scale(1.1);
            box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.4), 0 2px 4px -2px rgba(59, 130, 246, 0.4);
        }

        /* Dynamic Grid Layout for Input */
        #input-matrix {
            display: grid;
        }
        /* Dynamic Grid Layout for Output */
        #output-matrix {
            display: grid;
        }
    </style>
</head>
<body class="bg-gray-50 min-h-screen flex items-center justify-center p-4 font-sans">

    <div class="w-full max-w-6xl bg-white rounded-xl shadow-2xl p-6 md:p-10">
        <h1 class="text-3xl md:text-4xl font-extrabold text-gray-800 mb-2 text-center">
            Dynamic Max Pooling Visualization
        </h1>
        <p id="description" class="text-lg text-gray-600 mb-6 text-center">
            Adjust the parameters below to explore how different Pooling layers downsample the feature map.
        </p>

        <!-- Parameter Controls -->
        <div class="flex flex-wrap justify-center gap-4 mb-8 p-4 bg-gray-100 rounded-lg shadow-inner">
            <div class="flex flex-col">
                <label for="input-select" class="text-sm font-medium text-gray-700 mb-1">Input Size (I)</label>
                <select id="input-select" class="p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500">
                    <option value="4">4x4</option>
                    <option value="6">6x6</option>
                    <option value="8">8x8</option>
                </select>
            </div>
            <div class="flex flex-col">
                <label for="kernel-select" class="text-sm font-medium text-gray-700 mb-1">Kernel Size (K)</label>
                <select id="kernel-select" class="p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500">
                    <option value="2">2x2</option>
                    <option value="3">3x3</option>
                </select>
            </div>
            <div class="flex flex-col">
                <label for="stride-select" class="text-sm font-medium text-gray-700 mb-1">Stride (S)</label>
                <select id="stride-select" class="p-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500">
                    <option value="1">1</option>
                    <option value="2" selected>2</option>
                    <option value="3">3</option>
                </select>
            </div>
            <button id="apply-btn" class="self-end px-4 py-2 bg-purple-600 text-white font-bold rounded-lg hover:bg-purple-700 transition duration-300 shadow-md">
                Apply & Reset
            </button>
        </div>

        <div id="status-message" class="mt-4 mb-6 text-center text-lg font-medium text-green-700"></div>

        <div class="flex flex-col xl:flex-row justify-around items-center xl:items-start space-y-8 xl:space-y-0 xl:space-x-12">

            <!-- Input Feature Map -->
            <div class="text-center">
                <h2 id="input-title" class="text-2xl font-semibold text-gray-700 mb-4">Input Feature Map (4x4)</h2>
                <div id="input-matrix" class="shadow-xl rounded-lg overflow-hidden border-4 border-gray-300">
                    <!-- Cells will be generated by JS -->
                </div>
                <p id="params-summary" class="text-sm text-gray-500 mt-2">K=2, S=2</p>
            </div>

            <!-- Pooling Action Icon -->
            <div class="flex flex-col justify-center items-center h-full xl:pt-16">
                <svg id="arrow-icon" class="w-12 h-12 text-blue-500 transition-opacity duration-500 opacity-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                </svg>
                <p id="max-label" class="text-sm font-bold text-gray-800 mt-2 hidden">MAX IS:</p>
            </div>

            <!-- Output Pooled Feature Map -->
            <div class="text-center">
                <h2 id="output-title" class="text-2xl font-semibold text-gray-700 mb-4">Pooled Output (2x2)</h2>
                <div id="output-matrix" class="shadow-xl rounded-lg overflow-hidden border-4 border-blue-400">
                    <!-- Cells will be generated by JS -->
                </div>
            </div>
        </div>

        <!-- Controls -->
        <div class="mt-10 flex flex-col md:flex-row justify-center space-y-4 md:space-y-0 md:space-x-4">
            <button id="start-btn" class="px-6 py-3 bg-indigo-600 text-white font-bold rounded-lg hover:bg-indigo-700 transition duration-300 shadow-md">
                Start Animation
            </button>
            <button id="next-btn" class="px-6 py-3 bg-gray-400 text-white font-bold rounded-lg cursor-not-allowed transition duration-300 shadow-md" disabled>
                Next Step
            </button>
            <button id="reset-btn" class="px-6 py-3 bg-red-500 text-white font-bold rounded-lg hover:bg-red-600 transition duration-300 shadow-md">
                Reset
            </button>
        </div>
    </div>

    <script>
        const inputMatrixEl = document.getElementById('input-matrix');
        const outputMatrixEl = document.getElementById('output-matrix');
        const startBtn = document.getElementById('start-btn');
        const nextBtn = document.getElementById('next-btn');
        const resetBtn = document.getElementById('reset-btn');
        const applyBtn = document.getElementById('apply-btn');
        const statusMessageEl = document.getElementById('status-message');
        const arrowIcon = document.getElementById('arrow-icon');
        const maxLabel = document.getElementById('max-label');
        const inputTitleEl = document.getElementById('input-title');
        const outputTitleEl = document.getElementById('output-title');
        const paramsSummaryEl = document.getElementById('params-summary');

        // Global state variables (using window properties to avoid re-declaring consts)
        window.INPUT_SIZE = 4;
        window.KERNEL_SIZE = 2;
        window.STRIDE = 2;
        window.OUTPUT_SIZE = 2;
        window.inputData = []; // The feature map data
        window.outputData = []; // The pooled output data

        let step = 0; // Current pooling step (0 to total steps - 1)
        let isAnimating = false;
        
        // --- Core Functions ---

        // Function to generate random data for the input matrix
        function generateRandomInputData(size) {
            const data = [];
            for (let r = 0; r < size; r++) {
                const row = [];
                for (let c = 0; c < size; c++) {
                    // Generate random number between 0 and 99
                    row.push(Math.floor(Math.random() * 100) + 1); 
                }
                data.push(row);
            }
            window.inputData = data;
        }

        // Reads parameters, validates, calculates output size, and sets global state
        function validateAndCalculateOutput() {
            const inputEl = document.getElementById('input-select');
            const kernelEl = document.getElementById('kernel-select');
            const strideEl = document.getElementById('stride-select');

            const I = parseInt(inputEl.value);
            const K = parseInt(kernelEl.value);
            const S = parseInt(strideEl.value);
            
            // Check if input is smaller than kernel
            if (I < K) {
                statusMessageEl.textContent = "Error: Input Size (I) cannot be smaller than Kernel Size (K).";
                statusMessageEl.classList.remove('text-green-700');
                statusMessageEl.classList.add('text-red-600');
                return false;
            }

            // Check for exact output size (no padding assumed)
            // Output formula: (I - K) / S + 1
            const denominator = (I - K);
            if (denominator < 0 || denominator % S !== 0) {
                statusMessageEl.textContent = `Error: Invalid parameters! (Input Size ${I} - Kernel Size ${K}) = ${denominator}. This must be divisible by Stride ${S} for a valid output without padding.`;
                statusMessageEl.classList.remove('text-green-700');
                statusMessageEl.classList.add('text-red-600');
                return false;
            }

            const O = (denominator / S) + 1;
            
            // Set global parameters
            window.INPUT_SIZE = I;
            window.KERNEL_SIZE = K;
            window.STRIDE = S;
            window.OUTPUT_SIZE = O;

            statusMessageEl.textContent = `Valid Configuration: ${I}x${I} input maps to ${O}x${O} output. Click Start to proceed.`;
            statusMessageEl.classList.remove('text-red-600');
            statusMessageEl.classList.add('text-green-700');
            return true;
        }

        // Initializes the matrix grids in the DOM based on current global sizes
        function initializeGrids() {
            if (!validateAndCalculateOutput()) {
                inputMatrixEl.innerHTML = '<p class="p-4 text-gray-500">Input matrix generation failed due to invalid parameters.</p>';
                outputMatrixEl.innerHTML = '<p class="p-4 text-gray-500">Output matrix generation failed.</p>';
                resetControlStates(true);
                return;
            }

            // 1. Generate Input Data
            generateRandomInputData(window.INPUT_SIZE);

            // 2. Prepare Output Data Structure
            window.outputData = Array.from({ length: window.OUTPUT_SIZE }, () => Array(window.OUTPUT_SIZE).fill(''));

            // 3. Update Titles and Grid CSS
            inputTitleEl.textContent = `Input Feature Map (${window.INPUT_SIZE}x${window.INPUT_SIZE})`;
            outputTitleEl.textContent = `Pooled Output (${window.OUTPUT_SIZE}x${window.OUTPUT_SIZE})`;
            paramsSummaryEl.textContent = `K=${window.KERNEL_SIZE}, S=${window.STRIDE}`;
            
            inputMatrixEl.style.gridTemplateColumns = `repeat(${window.INPUT_SIZE}, minmax(0, 1fr))`;
            outputMatrixEl.style.gridTemplateColumns = `repeat(${window.OUTPUT_SIZE}, minmax(0, 1fr))`;

            // 4. Populate Input Matrix DOM
            inputMatrixEl.innerHTML = '';
            for (let r = 0; r < window.INPUT_SIZE; r++) {
                for (let c = 0; c < window.INPUT_SIZE; c++) {
                    const cell = document.createElement('div');
                    cell.className = 'grid-cell input-cell';
                    cell.textContent = window.inputData[r][c];
                    cell.id = `input-${r}-${c}`;
                    inputMatrixEl.appendChild(cell);
                }
            }

            // 5. Populate Output Matrix DOM
            outputMatrixEl.innerHTML = '';
            for (let r = 0; r < window.OUTPUT_SIZE; r++) {
                for (let c = 0; c < window.OUTPUT_SIZE; c++) {
                    const cell = document.createElement('div');
                    cell.className = 'grid-cell output-cell';
                    cell.textContent = '';
                    cell.id = `output-${r}-${c}`;
                    outputMatrixEl.appendChild(cell);
                }
            }
            
            resetControlStates(false); // Enable controls if initialization succeeded
        }

        // Manages button and status visibility after setup or reset
        function resetControlStates(isError) {
            step = 0;
            isAnimating = false;
            
            startBtn.disabled = isError;
            startBtn.textContent = 'Start Animation';
            startBtn.classList.toggle('bg-gray-400', isError);
            startBtn.classList.toggle('cursor-not-allowed', isError);
            startBtn.classList.toggle('bg-indigo-600', !isError);
            startBtn.classList.toggle('hover:bg-indigo-700', !isError);

            nextBtn.disabled = true;
            nextBtn.classList.remove('bg-indigo-600', 'hover:bg-indigo-700', 'cursor-pointer');
            nextBtn.classList.add('bg-gray-400', 'cursor-not-allowed');
            nextBtn.textContent = 'Next Step';

            arrowIcon.classList.add('opacity-0');
            maxLabel.classList.add('hidden');
        }
        
        // Highlights the current KxK pooling kernel and finds the max value
        function highlightKernel(startR, startC) {
            // Clear all previous highlights
            document.querySelectorAll('.input-cell').forEach(cell => {
                cell.classList.remove('active-kernel', 'max-value');
            });
            document.querySelectorAll('.output-cell').forEach(cell => {
                 // Only remove filled-output on kernel move if it's the current output target
            });
            
            let maxVal = -Infinity;
            let maxR = -1, maxC = -1;

            // Highlight the kernel cells and find the max value
            for (let r = 0; r < window.KERNEL_SIZE; r++) {
                for (let c = 0; c < window.KERNEL_SIZE; c++) {
                    const currentR = startR + r;
                    const currentC = startC + c;
                    
                    if (currentR < window.INPUT_SIZE && currentC < window.INPUT_SIZE) {
                        const value = window.inputData[currentR][currentC];
                        const cell = document.getElementById(`input-${currentR}-${currentC}`);
                        cell.classList.add('active-kernel');
                        
                        if (value > maxVal) {
                            maxVal = value;
                            maxR = currentR;
                            maxC = currentC;
                        }
                    }
                }
            }
            
            // Highlight the max value within the kernel
            if (maxR !== -1 && maxC !== -1) {
                 document.getElementById(`input-${maxR}-${maxC}`).classList.add('max-value');
                 return maxVal;
            }
            return -1; // Should not happen with validation
        }

        // Executes one step of the Max Pooling process
        function performStep() {
            if (step >= window.OUTPUT_SIZE * window.OUTPUT_SIZE) {
                statusMessageEl.textContent = `Animation Complete! The ${window.INPUT_SIZE}x${window.INPUT_SIZE} input is now a ${window.OUTPUT_SIZE}x${window.OUTPUT_SIZE} output.`;
                nextBtn.disabled = true;
                nextBtn.classList.add('bg-gray-400', 'cursor-not-allowed');
                nextBtn.classList.remove('bg-indigo-600', 'hover:bg-indigo-700');
                arrowIcon.classList.add('opacity-0');
                maxLabel.classList.add('hidden');
                return;
            }

            // Calculate current output indices
            const outputR = Math.floor(step / window.OUTPUT_SIZE);
            const outputC = step % window.OUTPUT_SIZE;
            
            // Calculate current kernel starting indices based on stride
            const startR = outputR * window.STRIDE; 
            const startC = outputC * window.STRIDE; 
            
            // 1. Highlight the current kernel and find max value
            const maxValue = highlightKernel(startR, startC);
            
            // 2. Update status and display max value
            statusMessageEl.textContent = `Step ${step + 1}: Finding the maximum value in the ${window.KERNEL_SIZE}x${window.KERNEL_SIZE} window (starts at [${startR}, ${startC}]). Max is ${maxValue}.`;
            maxLabel.textContent = `MAX IS: ${maxValue}`;
            maxLabel.classList.remove('hidden');
            
            // Clear previous output highlight to show movement
            document.querySelectorAll('.output-cell').forEach(cell => {
                cell.classList.remove('filled-output');
            });

            // 3. Update the output cell visually after a short delay
            const outputCell = document.getElementById(`output-${outputR}-${outputC}`);
            setTimeout(() => {
                arrowIcon.classList.remove('opacity-0');
                outputCell.textContent = maxValue;
                outputCell.classList.add('filled-output');
                window.outputData[outputR][outputC] = maxValue;
                
                // Clear the max highlight from input after it moves
                setTimeout(() => {
                    document.querySelectorAll('.input-cell').forEach(cell => {
                        cell.classList.remove('max-value');
                    });
                    arrowIcon.classList.add('opacity-0');
                }, 500); // Short delay to show transfer
            }, 600); // Delay for visualization effect
            
            step++;
            
            if (step === window.OUTPUT_SIZE * window.OUTPUT_SIZE) {
                nextBtn.textContent = 'Finish';
            } else {
                 nextBtn.textContent = 'Next Step';
            }
        }

        // --- Event Listeners ---
        
        startBtn.addEventListener('click', () => {
            if (!isAnimating && !startBtn.disabled) {
                isAnimating = true;
                startBtn.textContent = 'Animation Started';
                startBtn.disabled = true;
                startBtn.classList.remove('bg-indigo-600', 'hover:bg-indigo-700');
                startBtn.classList.add('bg-gray-400', 'cursor-not-allowed');

                nextBtn.disabled = false;
                nextBtn.classList.remove('bg-gray-400', 'cursor-not-allowed');
                nextBtn.classList.add('bg-indigo-600', 'hover:bg-indigo-700', 'cursor-pointer');
                
                performStep();
            }
        });

        nextBtn.addEventListener('click', () => {
             if (isAnimating && step <= window.OUTPUT_SIZE * window.OUTPUT_SIZE) {
                 performStep();
             }
        });

        // Use the Apply button to trigger setup/validation
        applyBtn.addEventListener('click', initializeGrids);
        resetBtn.addEventListener('click', initializeGrids); // Reset also runs initialization with current selections
        
        // Initial setup on load
        window.onload = initializeGrids;

    </script>
</body>
</html>
