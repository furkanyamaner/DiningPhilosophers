import threading
import time
import random

class DiningPhilosophers:
    def __init__(self, num_philosophers):
        self.num_philosophers = num_philosophers  # Filozof sayısını kaydediyoruz
        self.forks = [threading.Semaphore(1) for _ in range(num_philosophers)]  # Her çatal için bir semafor oluşturuyoruz
        self.philosophers = [threading.Thread(target=self.dine, args=(i,)) for i in range(num_philosophers)]  # Her filozof için bir thread oluşturuyoruz. (List Comprehension kullanılıyor.)
        self.running = True  # Programın çalışıp çalışmadığını kontrol etmek için bir bayrak tanımlıyoruz

    def start(self):
        for philosopher in self.philosophers:
            philosopher.start()  # Her filozofun thread'ini başlatıyoruz

    def stop(self):
        self.running = False  # Programı durdurmak için bayrağı False olarak ayarlıyoruz

    def dine(self, philosopher_id):
        while self.running:  # Program çalışırken
            self.think(philosopher_id)  # Filozofun düşünme işlemini gerçekleştiriyoruz
            self.eat(philosopher_id)  # Filozofun yeme işlemini gerçekleştiriyoruz

    def think(self, philosopher_id):
        print(f"Philosopher {philosopher_id} is thinking.")  # Filozofun düşündüğünü ekrana yazdırıyoruz
        time.sleep(random.uniform(1, 3))  # Rastgele bir süre boyunca filozofun düşünmesini bekliyoruz

    def eat(self, philosopher_id):
        left_fork = philosopher_id  # Sol çatalın indeksi filozofun kendi indeksiyle aynı
        right_fork = (philosopher_id + 1) % self.num_philosophers  # Sağ çatalın indeksi, bir sonraki filozofun indeksi olacak şekilde mod alınmış şekilde hesaplanır

        # Çataları almaya çalışıyoruz
        self.forks[left_fork].acquire()  # Sol çatalı almaya çalışıyoruz
        self.forks[right_fork].acquire()  # Sağ çatalı almaya çalışıyoruz

        print(f"Philosopher {philosopher_id} is eating.")  # Filozofun yemek yediğini ekrana yazdırıyoruz
        time.sleep(random.uniform(1, 3))  # Rastgele bir süre boyunca filozofun yemesini bekliyoruz

        # Çataları geri bırakıyoruz
        self.forks[left_fork].release()  # Sol çatalı geri bırakıyoruz
        self.forks[right_fork].release()  # Sağ çatalı geri bırakıyoruz


if __name__ == "__main__":
    num_philosophers = 5  # Filozof sayısı
    dining_table = DiningPhilosophers(num_philosophers) # Yemek masası oluşturuyoruz
    dining_table.start()  # Yemek masasını başlatıyoruz

    try:
        time.sleep(10)  # Filozofların 10 saniye boyunca yemek yemesini bekliyoruz
    finally:
        dining_table.stop()  # Programı durduruyoruz
        
        
        
