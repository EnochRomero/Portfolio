using System;

class Program
{
    static void Main(string[] args)
    {
        static void DisplayMenu()
        {
            Console.WriteLine("Please Select One of the Following Activities:");
            Console.WriteLine("1. Breathing");
            Console.WriteLine("2. Relfecting");
            Console.WriteLine("3. Listing");
            Console.WriteLine("4. Quit");
        }

        string choice = "0";

        while (choice != "4")
        {
            DisplayMenu();
            choice = Console.ReadLine();

            if (choice == "1")
            {
                Console.Clear();
                Breathing breathing = new Breathing();

                breathing.SetDesc("In this acticty you will breath in, hold your breath, and breath out as directed.");
                breathing.SetTitle("Breathing Acticity");

                breathing.DisplayIntro();
                breathing.BreathingActivity();
                breathing.DisplayOutro();

            }

            
            if (choice == "2")
            {
                Console.Clear();
                Reflecting reflecting = new Reflecting();

                reflecting.SetDesc("In this activity you will be given questions to reflect on an experience you have had.");
                reflecting.SetTitle("Reflecting Activity");

                reflecting.DisplayIntro();
                reflecting.ReflectingActicity();
                reflecting.DisplayOutro();
            }

            if (choice == "3")
            {
                Console.Clear();
                Listing listing = new Listing();

                listing.SetDesc("In this activity you will given a prompt and then you have to answer that prompt before the time runs out.");
                listing.SetTitle("Listing Activity");

                listing.DisplayIntro();
                listing.ListingActicity();
                listing.DisplayOutro();
            } 

        }
    }
}