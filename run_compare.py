from cli import CommandLineInterface
from compare import Compare
from datetime import date, timedelta,datetime


if __name__ == "__main__":

    current_date = datetime.today()
    print("Start time: {}".format(current_date))
    print(" -------------------(´・(oo)・｀)---------------------------------")
    cli = CommandLineInterface()
    args = cli.get_arguments()

    firstenv = args.get('firstenv')
    secondenv = args.get('secondenv')
    inputfile = args.get('inputfile')

    compare = Compare(firstenv, secondenv, inputfile )
    compare.compare_values()
    finished_time = datetime.today()
    print("---------------------(´・(oo)・｀)-------------------------------")
    print("End Time: {}".format(finished_time))
    print("Elapsed Time: {}".format(finished_time - current_date) )

