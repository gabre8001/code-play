package baseball;

import nextstep.utils.Console;

public class Application {
    public static void main(String[] args) {
        // TODO 숫자 야구 게임 구현
        Controller game = new Controller();
        while(true) {
            game.run();
        }
    }
}
