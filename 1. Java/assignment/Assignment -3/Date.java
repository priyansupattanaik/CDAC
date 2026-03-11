import java.util.Scanner;
class DateMethods {
    int day;
    int month;
    int year;
    DateMethods(int d, int m, int y) {
        day = d;
        month = m;
        year = y;
    }
    public boolean isLeapYear() {
        if (year % 400 == 0) {
            return true;
        } else if (year % 100 == 0) {
            return false;
        } else if (year % 4 == 0) {
            return true;
        } else {
            return false;
        }
    }
    public boolean isValid() {
        if (year < 1 || month < 1 || month > 12 || day < 1) {
            return false;
        }
        int[] days = {31, isLeapYear() ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (day > days[month - 1]) {
            return false;
        }

        return true;
    }
    public int getDayOfWeek() {
        int d = day;
        int m = month;
        int y = year;
        if (m < 3) {
            m = m + 12;
            y = y - 1;
        }
        int k = y % 100;
        int j = y / 100;
        int h = (d + (13 * (m + 1)) / 5 + k + (k / 4) + (j / 4) + (5 * j)) % 7;
        int result = (h + 6) % 7;
        return result;
    }
    public DateMethods getNextDay() {
        int[] days = {31, isLeapYear() ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int nd = day + 1;
        int nm = month;
        int ny = year;
        if (nd > days[month - 1]) {
            nd = 1;
            nm++;
            if (nm > 12) {
                nm = 1;
                ny++;
            }
        }

        return new DateMethods(nd, nm, ny);
    }
    public DateMethods getPreviousDay() {
        int nd = day - 1;
        int nm = month;
        int ny = year;
        if (nd < 1) {
            nm--;
            if (nm < 1) {
                nm = 12;
                ny--;
            }
            int[] days = {31, (ny % 400 == 0 || (ny % 4 == 0 && ny % 100 != 0)) ? 29 : 28,
                    31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
            nd = days[nm - 1];
        }
        return new DateMethods(nd, nm, ny);
    }
    public String toString() {
        String d = (day < 10 ? "0" + day : "" + day);
        String m = (month < 10 ? "0" + month : "" + month);
        return d + "-" + m + "-" + year;
    }
}
public class Date {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter day: ");
        int d = sc.nextInt();
        System.out.print("Enter month: ");
        int m = sc.nextInt();
        System.out.print("Enter year: ");
        int y = sc.nextInt();
        DateMethods date = new DateMethods(d, m, y);
        System.out.println("Is the date valid? " + date.isValid());
        System.out.println("Day of the week (0=Sunday ... 6=Saturday): " + date.getDayOfWeek());
        System.out.println("Is it a leap year? " + date.isLeapYear());
        DateMethods next = date.getNextDay();
        System.out.println("Next day is: " + next);
        DateMethods prev = date.getPreviousDay();
        System.out.println("Previous day is: " + prev);
    }
}
