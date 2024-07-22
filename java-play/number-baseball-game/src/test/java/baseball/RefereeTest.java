package baseball;

import nextstep.test.NSTest;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class RefereeTest {
    Referee referee = new Referee();

    @Test
    void 스트라이크() {
        referee.setRandomNumber("123");
        assertThat(referee.checkStrike("123")).isEqualTo(3);
        assertThat(referee.checkStrike("124")).isEqualTo(2);
        assertThat(referee.checkStrike("423")).isEqualTo(2);
        assertThat(referee.checkStrike("143")).isEqualTo(2);
        assertThat(referee.checkStrike("144")).isEqualTo(1);
        assertThat(referee.checkStrike("424")).isEqualTo(1);
        assertThat(referee.checkStrike("443")).isEqualTo(1);
        assertThat(referee.checkStrike("444")).isEqualTo(0);
    }

    @Test
    void 볼() {
        referee.setRandomNumber("123");
        assertThat(referee.checkBall("123")).isEqualTo(0);
        assertThat(referee.checkBall("244")).isEqualTo(1);
        assertThat(referee.checkBall("441")).isEqualTo(1);
        assertThat(referee.checkBall("344")).isEqualTo(1);
        assertThat(referee.checkBall("321")).isEqualTo(2);
        assertThat(referee.checkBall("443")).isEqualTo(0);
        assertThat(referee.checkBall("213")).isEqualTo(2);
        assertThat(referee.checkBall("231")).isEqualTo(3);
    }

}
