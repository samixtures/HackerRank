// # Given a non-negative integer x, return its square root.
// # Note: You may not use a built in square root function and decimals should be truncated to return an integer value.

// # Ex: Given the following x...

// # x = 9, return 3.
// # Ex: Given the following x...

// # x = 12, return 3.

// Hello World! program
namespace HelloWorld
{
    class Hello
    {
        static void Main(string[] args)
        {
            System.Console.WriteLine("Hello World!");
        }
        static double SquareRoot(int x)
        {
            if (x >= 0)
            {
                Math.Sqrt(x);
            }
            else
            {
                return 0.0;
            }
        }
    }
}
