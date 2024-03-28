// Motor 1 (Left Front)
int motor1Pin1 = 6;
int motor1Pin2 = 7;

// Motor 2 (Left Rear)
int motor2Pin1 = 8;
int motor2Pin2 = 9;

int angle;
int dist;
String readString;


void goForward(int time_number_of_loop) {
  // Set both left and right motors to move forward
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);

  delay(time_number_of_loop);
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);

}

void goBackward(int time_number_of_loop ) {
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH);

  delay(time_number_of_loop);
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);

}

void turnLeft(int time_number_of_loop) {
  // Set left motors backward and right motors forward for turning left
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH);
 
  delay(time_number_of_loop);
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);

}

void turnRight(int time_number_of_loop) {
  // Set left motors forward and right motors backward for turning right
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);

  delay(time_number_of_loop);
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);

}

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  // Initialize all motor pins as outputs
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(motor2Pin1, OUTPUT);
  pinMode(motor2Pin2, OUTPUT);

}

void  loop() {
  while (!Serial.available());
  readString = Serial.readString();
  // 3 characters - angle
  // 3 characters - distance
  angle = readString.substring(0, 3).toInt();
  dist = readString.substring(3, 7).toInt();

  turnRight(angle * 10);
  goForward(dist * 10);

}


