
import org.junit.jupiter.api.Test;

import java.nio.file.Files;
import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.*;

public class RegistrationFormTest {

    private String readHtml() throws Exception {
        return Files.readString(Path.of("index.html"));
    }

    @Test
    void testRegistrationFormExists() throws Exception {
        assertTrue(
            readHtml().contains("id=\"registrationForm\""),
            "Registration form is missing"
        );
    }

    @Test
    void testStudentNameExists() throws Exception {
        assertTrue(
            readHtml().contains("id=\"studentName\""),
            "Student Name field is missing"
        );
    }

    @Test
    void testRollNumberExists() throws Exception {
        assertTrue(
            readHtml().contains("id=\"rollNumber\""),
            "Roll Number field is missing"
        );
    }

    @Test
    void testEmailExists() throws Exception {
        assertTrue(
            readHtml().contains("id=\"email\""),
            "Email field is missing"
        );
    }

    @Test
    void testCourseExists() throws Exception {
        assertTrue(
            readHtml().contains("id=\"course\""),
            "Course field is missing"
        );
    }

    @Test
    void testSubmitButtonExists() throws Exception {
        assertTrue(
            readHtml().contains("type=\"submit\""),
            "Submit button is missing"
        );
    }
}
