# Brocard's Extended Problem
A computational study of Brocard's Extended Problem.

# Background
Brocard's Problem questions how many perfect squares arise from n!+1, where n is an integer.
Mathematically, Brocard's Problem is n!+1=m^2, where n and m are integers.
There are only 3 known solutions to Brocard's Problem: n=4, 5, 7 and m=5, 11, 71, respectively.
Here, I extend Brocard's Problem to question how many perfect squares arise from n!+i, where i is an integer.
Mathematically, the Extended Brocard's Problem is n!+i=m^2, where n, i, and m are integers.
This computational study finds patterns in Brocard's Extended Problem, potentially useful in determining how many solutions to Brocard's Problem exist.
For more information, see https://en.wikipedia.org/wiki/Brocard%27s_problem.

# Setup
1. Install Python at https://www.python.org/downloads/.
2. Download repository.
3. Open Terminal in repository folder.
4. Enter ```pip install numpy```.
5. Enter ```pip install matplotlib```.
6. Enter ```python main.py```.

# Usage
Run *main.py* via ```python main.py``` in Terminal.
```n max:``` will print.
Enter the maximum number of factorials to check.
After, ```i max:``` will print.
Enter the maximum number of integers to check.

After, the program will check all combinations of ```n``` and ```i``` to find solutions m to Brocard's Extended Problem.
Solutions print in the form ```n, i, m```, and save to the file *solutions.txt*
After checking all ```i``` for specified ```n```, three plots will open.

The first plot is the number of solutions found per ```i``` between n=1 and maximum entered n.
The second plot is an inverse fourier transform of the first plot.
The motivation behind the inverse fourier transform is the frequency-like spikes the first plot contains.
In this sense, the second plot is "Brocard's Wave."
The third plot is a three-dimensional visualization of all solutions (n, i, m) to Brocard's Extended Problem found.

# Example
Suppose the user wants to check n to one hundred (100) and i to one million (1000000).
Run *main.py* via ```python main.py``` in Terminal.
When ```n max:``` prints, enter ```100```.
When ```i max:``` prints, enter ```1000000```.

After, all solutions the program finds will print.
The results of this computational study (specified in the example) are located in the repository as *Figure_0.png*, *Figure_1.png*, *Figure_2.png*, and *solutions.txt*.

# Errors
1. ```Enter integer n_max:```
Solution: Enter integer value for maximum n.
2. ```Enter integer i_max:```
Solution: Enter integer value for maximum i.

# Contact
For help, improvements, etc., feel free to contact **silveryystar** on Discord.
