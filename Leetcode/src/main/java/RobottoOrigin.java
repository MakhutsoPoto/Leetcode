public class RobottoOrigin {
    public boolean judgeCircle(String moves) {
        int x= 0;
        int y = 0;
        for (char move : moves.toCharArray()) {
            if (move == 'U') {
                x+= 1;
            }else if(move == 'D'){
                x -= 1;
            }else if (move == 'L') {
               y -= 1;
            } else if (move == 'R'){
             y += 1 ;
            }
        }if(x == 0 && y == 0){
           return true;
       }else {return false;
          }
}
}
