package baseball;

public class GameEvent {
    GameState state;
    BallState ball;

    public void setState(GameState state) {
        this.state = state;
    }

    public void setBall(BallState ball) {
        this.ball = ball;
    }

    public GameState getState() {
        return state;
    }

    public BallState getBall() {
        return ball;
    }

}
