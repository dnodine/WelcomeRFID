# WelcomeRFID
Setting up Raspbian for the RFID RC522

Before we begin the process of utilizing the RFID RC522 on our Raspberry Pi, we will first have to make changes to its configuration. By default, the Raspberry Pi has the SPI (Serial Peripheral Interface) disabled, which is a bit of a problem as that is what our RFID reader circuit runs through.
Don’t worry though as it is fairly simple to re-enable this interface, just follow our steps below to configure your Raspberry Pi and Raspbian to utilize the SPI interface.

    1. Let’s begin by first opening the raspi-config tool, and we can do this by opening the terminal and running the following command.
            sudo raspi-config
    
    2. Select “5 Interfacing Options“. Once you have this option selected, press Enter.

    3. Select “P4 SPI“, again press Enter to select the option once it is highlighted.
    
    4. You will now be asked if you want to enable the SPI Interface, select Yes with your arrow keys and press Enter to proceed.
    
    5. To get back to the terminal by pressing Enter and then ESC then reboot your pi
    
    6. Run the following command to see if spi_bcm2835 is listed.
            lsmod | grep spi
            
    7. Run the following two commands on your Raspberry Pi to update it.
            sudo apt-get update
            sudo apt-get upgrade

    8. Run the following command to install all of the required packages for this guide on setting up your RFID reader.
            sudo apt-get install python2.7-dev python-pip git
    9. Run the following command  on your Raspberry Pi to install spidev to your Raspberry Pi through pip.
            sudo pip install spidev


Credit for this project goes to https://pimylifeup.com/raspberry-pi-rfid-rc522/
