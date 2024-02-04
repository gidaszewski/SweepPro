
![Logo](https://res.cloudinary.com/dtcfj52hr/image/upload/v1706988090/Sweep%20Pro%20Website/vjcushjrjxa1dn76gtah.png)


# Sweep Pro

App for keep clean and organized your Downloads folder. When you run the app, it will move all your files into different folders depending on their extension.
https://sweep-pro.tech/


## Automatize your file

Go from this

![Logo](https://res.cloudinary.com/dtcfj52hr/image/upload/v1707086927/Sweep%20Pro%20Website/maxij7rztm10vofict24.png)

To this

![Logo](https://res.cloudinary.com/dtcfj52hr/image/upload/v1707086926/Sweep%20Pro%20Website/satabiy70hdggmis5kfc.png)



## Installation

You need to have Python on your computer before running the application.
https://www.python.org/downloads/macos/

Clone the SweepPro GitHub Repository or download the app folder in your computer.

```bash
  ~ git clone https://github.com/gidaszewski/SweepPro
```

Run the following code in your terminal. It will create a shell ejecute script.

```bash
  ~ sudo nano sweep.sh
```

Add the following lines in the sweep.sh script. You should modify 'YOUR-USER' with your current username.

```bash
  #!/bin/zsh

  cd /Users/YOUR-USER/SweepPro

  python3 cleaner.py
```

Press "Ctrl + X" for close and save the script, then press "Y" and "Enter" for finish.

## Run

Run the following code in your terminal.

```bash
  ~ sh sweep.sh
```

Move any file to your Downloads folder for activating the program. Enjoy!
    
## Tech Stack

Python, Linux


## License

[MIT](https://github.com/gidaszewski/SweepPro/blob/master/LISENSE)

This readme was created with readme.so :)

