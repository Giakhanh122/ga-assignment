# GA Assignment

**Tên:** Võ Văn Gia Khánh  
**Mã sinh viên:** 2411549

## 1. Giới thiệu

Thuật toán Genetic Algorithm (GA) được lấy cảm hứng bởi quá trình **chọn lọc tự nhiên** của Charles Darwin. Các cá thể phù hợp nhất sẽ được giữ lại, giao phối và tạo ra thế hệ mới — ngày càng tối ưu hơn theo thời gian.

GA thuộc nhóm **Metaheuristic** — không đảm bảo tìm được tối ưu toàn cục nhưng cho nghiệm tốt trong thời gian hợp lý với bài toán NP-hard.

---

## 2. Vòng lặp GA

```
Khởi tạo quần thể ngẫu nhiên
        ↓
  Đánh giá fitness
        ↓
  Điều kiện dừng? ──→ YES → Trả kết quả
        ↓ NO
    Chọn lọc
        ↓
    Lai ghép
        ↓
    Đột biến
        ↓
  Thay thế quần thể
        ↓
  (lặp lại)
```

### 2.1 Khởi tạo (Initialization)

Tạo ngẫu nhiên `N` nhiễm sắc thể (chromosome), mỗi cái là một lời giải tiềm năng. Với bài toán nhị phân, mỗi chromosome là chuỗi bit:

```
Chromosome: [1, 0, 1, 1, 0, 1, 1, 0]
```

### 2.2 Đánh giá Fitness (Evaluation)

Tính hàm thích nghi `f(x)` cho từng cá thể. Cá thể có `f(x)` cao hơn có cơ hội sinh sản cao hơn.

### 2.3 Chọn lọc (Selection)

**Tournament Selection** (được dùng trong cả hai implementation):

Chọn ngẫu nhiên `tournament_size = 3` cá thể, lấy cá thể có fitness cao nhất trong nhóm đó làm cha/mẹ.

```python
tournament = random.sample(population, k=3)
best = max(tournament, key=fitness_function)
```

### 2.4 Lai ghép (Crossover)

**Single-point crossover**:

```
Cha A: [1, 0, 1, 1 | 0, 1, 1, 0]
Cha B: [0, 0, 1, 0 | 1, 0, 0, 1]
                  ↓ point = random
Con C: [1, 0, 1, 1 | 1, 0, 0, 1]  ← trái từ A, phải từ B
Con D: [0, 0, 1, 0 | 0, 1, 1, 0]  ← trái từ B, phải từ A
```

### 2.5 Đột biến (Mutation)

Mỗi bit bị lật với xác suất `p_m = 1/L` (L = độ dài chromosome):

```
Trước: [1, 0, 1, 1, 0, 1, 1, 0]
                        ↑
Sau:   [1, 0, 1, 1, 1, 1, 1, 0]   ← bit index 4 bị lật 0→1
```

### 2.6 Thay thế (Replacement)

Trong FP: Thay thế toàn bộ quần thể bằng offspring từ selection, crossover, mutation.

Trong OOP: **Elitism** - Giữ lại 1 cá thể tốt nhất từ thế hệ cũ, phần còn lại thay bằng offspring.

---

## 3. Tham số mặc định

Cả hai implementation sử dụng chung bộ hằng số:

| Tham số           | Giá trị mặc định | Ý nghĩa                |
| ----------------- | ---------------- | ---------------------- |
| `population_size` | 100              | Kích thước quần thể    |
| `generations`     | 300              | Số thế hệ tối đa       |
| `mutation_prob`   | `"1/L"`          | Tự động = `1 / length` |
| `tournament_size` | 3                | Kích thước tournament  |
| `seed`            | 42               | Random seed            |

---

## 4. Kiến trúc Implementation

Có hai phiên bản triển khai GA với cùng logic nhưng khác nhau về thiết kế:

### 4.1 OOP-based (`oop/`) — Hướng đối tượng

Tổ chức code theo các class, mỗi thành phần là một đối tượng riêng biệt.

```
GeneticAlgorithm          ← Class trung tâm, chứa config & vòng lặp chính
├── Chromosome            ← Bọc list genes + phương thức fitness
├── Population            ← Bọc list[Chromosome]
├── SelectionStrategy     ← Tournament selection
├── CrossoverStrategy     ← Single-point crossover
└── MutationStrategy      ← Bit-flip mutation
```

**Cách sử dụng:**

```python
from oop.run import run_one_max

result = run_one_max(length=10)
print(result)  # ([1,1,1,...], fitness, history, runtime)
```

### 4.2 Functional-based (`fp/`) — Hướng hàm

Tổ chức code theo các hàm thuần túy (pure functions), không có class.

```
run_one_max() / run_knap_sack()  ← Entry points
├── create_chromosome()         ← list[int]
├── fitness()                   ← Hàm tính fitness
├── selection()                 ← Tournament, trả về chromosome
├── crossover()                 ← Single-point, trả về 2 con
├── mutate()                    ← Bit-flip, trả về chromosome mới
├── next_generation()           ← Tạo thế hệ mới
└── ga()                        ← Vòng lặp chính với reduce
```

**Cách sử dụng:**

```python
from fp.run import run_one_max

result = run_one_max(length=10)
print(result)  # ([1,1,1,...], fitness, history, runtime)
```

### 4.3 So sánh hai phiên bản

| Tiêu chí | OOP (`oop/`)      | Functional (`fp/`) |
| -------- | ----------------- | ------------------ |
| Thiết kế | Class & objects   | Pure functions     |
| Elitism  | Có (giữ best)     | Không              |
| State    | Lưu trong objects | Trả về qua tuples  |
| Test     | Mock objects      | Test từng hàm      |
| Mở rộng  | Kế thừa classes   | Thay đổi functions |

Cả hai cho **kết quả tương tự** khi dùng cùng `seed` và tham số.

---

## 5. OneMax Problem

### 5.1 Định nghĩa

Cho chuỗi nhị phân độ dài `n`, tìm chuỗi có **số bit 1 nhiều nhất**.

```
Hàm mục tiêu:  f(x) = Σ xᵢ  (i = 1..n)
Nghiệm tối ưu: x* = [1, 1, 1, ..., 1]  →  f(x*) = n
```

Đây là bài toán benchmark đơn giản nhất — dùng để kiểm tra GA hoạt động đúng.

### 5.2 Fitness Function

```python
def fitness(bits):   # FP
    return sum(bits)

def onemax_fitness(self):  # OOP
    return sum(self.individual)
```

### 5.3 Ví dụ (n = 8)

```
Cá thể A: [1, 0, 1, 1, 0, 1, 1, 0]  →  f = 5
Cá thể B: [0, 0, 1, 0, 1, 0, 0, 1]  →  f = 3
Tối ưu:   [1, 1, 1, 1, 1, 1, 1, 1]  →  f = 8  ← GA tìm được
```

### 5.4 Hội tụ

Với OneMax (n=100), GA thường đạt nghiệm tối ưu sau khoảng **50–100 thế hệ** với quần thể 100 cá thể.

---

## 6. 0/1 Knapsack Problem

### 6.1 Định nghĩa

Có `n` vật phẩm, mỗi vật có trọng lượng `wᵢ` và giá trị `vᵢ`. Ba lô chứa tối đa `W` kg. Chọn tập vật phẩm để **tổng giá trị lớn nhất** mà không vượt giới hạn.

```
maximize:   Σ vᵢ · xᵢ
subject to: Σ wᵢ · xᵢ ≤ W
            xᵢ ∈ {0, 1}
```

Đây là bài toán **NP-hard** — không có thuật toán đa thức nào giải tối ưu.

### 6.2 Ví dụ (5 vật phẩm, W = 10 kg)

| #   | Vật phẩm  | Giá trị `v` | Trọng lượng `w` |
| --- | --------- | ----------- | --------------- |
| 0   | Kim cương | 10          | 3               |
| 1   | Sách      | 4           | 5               |
| 2   | Laptop    | 8           | 4               |
| 3   | Đồ nghề   | 3           | 6               |
| 4   | Đồng hồ   | 5           | 2               |

```
Chromosome: [1, 0, 1, 0, 1]   ← chọn Kim cương, Laptop, Đồng hồ

Tổng trọng lượng: 3 + 4 + 2 = 9 kg ≤ 10 ✓
Tổng giá trị:     10 + 8 + 5 = 23  ← optimal!
```

### 6.3 Fitness Function với Penalty

Nếu vượt capacity, fitness = 0 (FP) hoặc 0 (OOP).

```python
def fitness(chromosome, weights, values, capacity):  # FP
    cap = sum(weights[i] for i in range(len(chromosome)) if chromosome[i])
    val = sum(values[i] for i in range(len(chromosome)) if chromosome[i])
    return val if cap <= capacity else 0

def knapsack_fitness(self, items):  # OOP
    cap = sum(items.weights[i] * self.individual[i] for i in range(len(self.individual)))
    val = sum(items.values[i] * self.individual[i] for i in range(len(self.individual)))
    return val if cap <= items.calculateCapacity() else 0
```

### 6.4 Implementation

```python
# FP
from fp.run import run_knap_sack
result = run_knap_sack(length=5)

# OOP
from oop.run import run_knap_sack
result = run_knap_sack(length=5)
```

---

## 7. So sánh GA với các thuật toán khác

### OneMax

| Thuật toán    | Độ phức tạp    | Ghi chú                 |
| ------------- | -------------- | ----------------------- |
| Brute Force   | O(2ⁿ)          | Không khả thi với n lớn |
| Hill Climbing | O(n²)          | Dễ kẹt local optima     |
| **GA**        | O(gen × N × n) | Tốt, linh hoạt          |

### Knapsack

| Thuật toán          | Độ phức tạp    | Tối ưu toàn cục                  |
| ------------------- | -------------- | -------------------------------- |
| Brute Force         | O(2ⁿ)          | Có                               |
| Dynamic Programming | O(n × W)       | Có — nhưng chậm khi W lớn        |
| Greedy              | O(n log n)     | Không đảm bảo                    |
| **GA**              | O(gen × N × n) | Không đảm bảo — nhưng nghiệm tốt |

GA đặc biệt hiệu quả khi **W rất lớn** hoặc bài toán có nhiều ràng buộc phức tạp.

---

## 8. Ưu điểm & Hạn chế

### Ưu điểm

- Không cần thông tin gradient — áp dụng cho hàm mục tiêu không liên tục, không khả vi
- Khám phá không gian tìm kiếm song song (nhiều cá thể cùng lúc)
- Linh hoạt: chỉ cần thay fitness function là áp dụng cho bài toán mới
- Reproducible hoàn toàn nhờ `seed` cố định
- Dễ song song hóa (parallel GA)

### Hạn chế

- Không đảm bảo tìm nghiệm tối ưu toàn cục
- Cần tinh chỉnh tham số (`N`, `p_m`, `tournament_size`) cho từng bài toán
- Hội tụ sớm (premature convergence) nếu đa dạng gen giảm quá nhanh
- Chậm hơn các thuật toán chuyên dụng trên bài toán đơn giản

---

## 9. Tài liệu tham khảo

- Holland, J.H. (1975). _Adaptation in Natural and Artificial Systems_. MIT Press.
- Goldberg, D.E. (1989). _Genetic Algorithms in Search, Optimization, and Machine Learning_. Addison-Wesley.
- Mitchell, M. (1998). _An Introduction to Genetic Algorithms_. MIT Press.

---

## Cấu trúc dự án

- `fp/`: triển khai theo phong cách lập trình hàm
  - `run.py`: điểm vào để thực thi OneMax và Knapsack
  - `src/`: các triển khai thuật toán và trợ giúp
- `oop/`: triển khai theo hướng đối tượng
  - `run.py`: điểm vào để thực thi OneMax và Knapsack
  - `src/`: các lớp thuật toán và trợ giúp
- `tests/`: script test manual để chạy OneMax và Knapsack
- `fp/tests/`: script test manual dành riêng cho triển khai FP
- `oop/tests/`: script test manual dành riêng cho triển khai OOP

## Thiết lập môi trường

Phiên bản Python khuyến nghị: `3.13.x`.

Tạo và kích hoạt môi trường ảo:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Cài đặt các gói cần thiết:

```bash
python -m pip install pytest matplotlib
```

Nếu chỉ cần chạy script manual và không cần vẽ biểu đồ, `matplotlib` là tùy chọn.

Một số môi trường sử dụng backend matplotlib không tương tác. Trong trường hợp đó, script vẫn chạy nhưng biểu đồ sẽ bị tắt.

## Chạy script test manual

Từ thư mục gốc của kho lưu trữ, chạy:

```bash
python tests/test_onemax.py
python tests/test_knapsack.py
```

Hoặc cho test dành riêng cho FP:

```bash
python fp/tests/test_onemax.py
python fp/tests/test_knapsack.py
```

Hoặc cho test dành riêng cho OOP:

```bash
python oop/tests/test_onemax.py
python oop/tests/test_knapsack.py
```

Mỗi file là script độc lập với hàm `main()`.

## Nhóm test

Các script cung cấp ba mức thực thi:

- `small`
- `medium`
- `large`

Mỗi mức được định nghĩa trong script. Bạn có thể chọn tập con các trường hợp bằng cách chỉnh sửa danh sách `SELECTED_LEVELS` ở đầu file.

## Giải thích output

Các script in cấu hình thuật toán và kết quả cuối cùng cho mỗi mức.

- `best_fitness`: fitness tính toán của chromosome tốt nhất trả về.
- `best_solution`: chromosome nhị phân đại diện cho giải pháp.
- `history length`: số thế hệ được ghi lại.
- `runtime`: thời gian thực thi cho trường hợp test.
- `selected_indices` (Knapsack): chỉ số của item được chọn.
- `total_weight` / `total_value`: xác thực giải pháp knapsack tốt nhất.

Nếu `matplotlib` được cài đặt, script sẽ hiển thị biểu đồ fitness theo thế hệ.

- các tham số thuật toán
- In chi tiết kết quả:
  - `best_fitness`
  - `best_solution`
  - chỉ số item được chọn
  - tổng trọng lượng và tổng giá trị
  - tính hợp lệ của giải pháp
  - `history length`
  - `runtime`
- Hiển thị biểu đồ lịch sử fitness nếu `matplotlib` được cài đặt.

### `oop/tests/test_onemax.py`

- Chạy thuật toán di truyền OOP OneMax cho các độ dài chromosome khác nhau.
- In chi tiết cấu hình:
  - `length`
  - `population`
  - `generations`
  - `mutation_prob`
  - `seed`
- In chi tiết kết quả:
  - `best_fitness`
  - `best_solution`
  - `history length`
  - `runtime`
- Hiển thị biểu đồ lịch sử fitness nếu `matplotlib` được cài đặt.

### `oop/tests/test_knapsack.py`

- Chạy thuật toán di truyền OOP Knapsack cho các kích thước bài toán khác nhau.
- Mỗi trường hợp sử dụng `weights`, `values`, và `capacity` xác định được tạo từ seed cố định.
- In chi tiết bài toán:
  - `weights` của item
  - `values` của item
  - `capacity`
  - `length`
  - các tham số thuật toán
- In chi tiết kết quả:
  - `best_fitness`
  - `best_solution`
  - chỉ số item được chọn
  - tổng trọng lượng và tổng giá trị
  - tính hợp lệ của giải pháp
  - `history length`
  - `runtime`
- Hiển thị biểu đồ lịch sử fitness nếu `matplotlib` được cài đặt.

## Giải thích thiết kế OOP và FP

### Thiết kế FP (Functional Programming)

Trong triển khai FP, thuật toán được xây dựng bằng các hàm thuần túy. Các hàm như `create_chromosome`, `fitness`, `selection`, `crossover`, `mutate` được định nghĩa riêng biệt và sử dụng `reduce` để lặp qua các thế hệ. Điều này giúp mã dễ kiểm tra và tái sử dụng, với ít trạng thái mutable.

### Thiết kế OOP (Object-Oriented Programming)

Trong triển khai OOP, thuật toán được tổ chức thành các lớp như `Chromosome`, `Population`, `GeneticAlgorithm`, `SelectionStrategy`, v.v. Điều này cho phép mở rộng dễ dàng thông qua kế thừa và encapsulation, làm cho mã dễ hiểu và bảo trì hơn cho các vấn đề phức tạp.

## Phản ánh và so sánh (≤500 từ)

| Tiêu chí             | FP                                                           | OOP                            |
| -------------------- | ------------------------------------------------------------ | ------------------------------ |
| **Độ dễ đọc**        | Cao cho các hàm đơn giản, nhưng có thể phức tạp với `reduce` | Cao với cấu trúc lớp rõ ràng   |
| **Khả năng mở rộng** | Khó mở rộng, cần sửa đổi hàm                                 | Dễ mở rộng qua kế thừa         |
| **Kiểm tra**         | Dễ kiểm tra hàm thuần túy                                    | Dễ kiểm tra với mock objects   |
| **Hiệu suất**        | Tương tự, nhưng có thể chậm hơn với recursion sâu            | Tương tự, tốt cho các vòng lặp |
| **Bảo trì**          | Khó với thay đổi lớn                                         | Dễ bảo trì với encapsulation   |

Cả hai paradigm đều hiệu quả cho thuật toán di truyền. FP phù hợp cho logic đơn giản và immutable, trong khi OOP tốt cho cấu trúc phức tạp và tái sử dụng. Trong dự án này, OOP dễ mở rộng hơn cho các biến thể thuật toán.

## Giải thích output

Các script in cấu hình thuật toán và kết quả cuối cùng cho mỗi mức.

- `best_fitness`: fitness tính toán của chromosome tốt nhất trả về.
- `best_solution`: chromosome nhị phân đại diện cho giải pháp.
- `history length`: số thế hệ được ghi lại.
- `runtime`: thời gian thực thi cho trường hợp test.
- `selected_indices` (Knapsack): chỉ số của item được chọn.
- `total_weight` / `total_value`: xác thực giải pháp knapsack tốt nhất.

Nếu `matplotlib` được cài đặt, script sẽ hiển thị biểu đồ fitness theo thế hệ.
