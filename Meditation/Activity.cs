

class Activity
{
    private string _title;

    private int _duration; 

    private string _desc;

    public int GetDuration()
    {
        return _duration;
    }

    public void SetDuration(int duration)
    {
        _duration = duration;
    }

    
    public string GetTitle()
    {
        return _title;
    }

    public void SetTitle(string title)
    {
        _title = title;
    }

    public string GetDesc()
    {
        return _desc;
    }

    public void SetDesc(string desc)
    {
        _desc = desc;
    }


    public void DisplayIntro()

    {
        Console.WriteLine($"Welcome to the {_title}");

        Console.WriteLine(_desc);

        Console.WriteLine("How long would you like this acticity to last in seconds?:");
        _duration = Convert.ToInt32(Console.ReadLine());
    }

        public void DisplayOutro()

    {
        Console.WriteLine($"Well Done!");

        DisplayLoadingAnimation(5);

        Console.WriteLine($"You have completed {_duration} seconds of the {_title}.");        
        DisplayLoadingAnimation(3);

        Console.Clear();

    }

    public void DisplayGetReady()
    {
        Console.Clear();
        Console.WriteLine("Get Ready...");
        DisplayLoadingAnimation(5);
        Console.Clear();
    }


    public void DisplayLoadingAnimation(int timeOfAnimation)
    {
        List<string> animation = new List<string> {"|", "/", "-", "\\"};

        DateTime startTime = DateTime.Now;
        DateTime endTime = startTime.AddSeconds(timeOfAnimation);

        while (DateTime.Now < endTime)
        {
            foreach (string s in animation)
            {
                Console.Write(s);
                Thread.Sleep(1000);
                Console.Write("\b \b");

            }

        }

    }

}