

class Breathing : Activity
{


    public void BreathingActivity()
    {
        DateTime startTime = DateTime.Now;
        DateTime endTime = startTime.AddSeconds(GetDuration());

        while (DateTime.Now < endTime)
        {

            int countDown = 4;

            Console.Write("Breath in...");
            while (countDown > -1)
            {
                Console.Write("\b \b");
                if (countDown >= 1) 
                { 
                    Console.Write(countDown);
                }
                Thread.Sleep(1000);
                countDown -= 1;
            }
            Console.WriteLine();

            countDown = 4;

            Console.Write("Hold your breath...");
            while (countDown > -1)
            {
                Console.Write("\b \b");
                if (countDown >= 1) 
                { 
                    Console.Write(countDown);
                }
                Thread.Sleep(1000);
                countDown -= 1;
            }
            Console.WriteLine();

            countDown = 4;

            Console.Write("Breath out...");
            while (countDown > -1)
            {
                Console.Write("\b \b");
                if (countDown >= 1) 
                { 
                    Console.Write(countDown);
                }
                Thread.Sleep(1000);
                countDown -= 1;
            }
            Console.WriteLine();

            Console.WriteLine();

            
        }
    }
}