# GA Assignment

**Tên:** Võ Văn Gia Khánh  
**Mã sinh viên:** 2411549

Triển khai thuật toán Genetic Algorithm cho 2 bài toán: - OneMax - 0/1
Knapsack

Có 2 phiên bản: - `fp/`: Functional Programming - `oop/`:
Object-Oriented Programming

------------------------------------------------------------------------

## Cấu trúc project

    fp/
      src/
        onemax.py
        knapsack.py
      tests/
        test_onemax.py
        test_knapsack.py
      run.py

    oop/
      src/
      tests/
        test_onemax.py
        test_knapsack.py
      run.py
    reports/
    result.json

-   `fp/`: triển khai theo phong cách hàm\
-   `oop/`: triển khai hướng đối tượng\
-   `fp/tests/`, `oop/tests/`: test riêng\
-   `reports/`: lưu plot và kết quả\
-   `result.json`: output
------------------------------------------------------------------------

## Kiến trúc Implementation

Có hai phiên bản triển khai GA với cùng logic nhưng khác nhau về thiết
kế.

### OOP-based (`oop/`) --- Hướng đối tượng

    GeneticAlgorithm
    ├── Chromosome
    ├── Population
    ├── SelectionStrategy
    ├── CrossoverStrategy
    └── MutationStrategy


------------------------------------------------------------------------

### Functional-based (`fp/`) --- Hướng hàm

    run_one_max() / run_knap_sack()
    ├── create_chromosome()
    ├── fitness()
    ├── selection()
    ├── crossover()
    ├── mutate()
    ├── next_generation()
    └── ga()
------------------------------------------------------------------------
## Giải thích thiết kế

### FP (Functional Programming)

Sử dụng các hàm thuần (`create_chromosome`, `fitness`, `selection`,
`crossover`, `mutate`) và `reduce` để lặp qua thế hệ.\
Ít state, dễ test, khó mở rộng lớn.

### OOP (Object-Oriented Programming)

Sử dụng các class (`Chromosome`, `Population`, `GeneticAlgorithm`,
...).\
Dễ mở rộng, rõ cấu trúc, phù hợp hệ thống lớn.

------------------------------------------------------------------------
## So sánh FP và OOP

  Tiêu chí   OOP (`oop/`)        Functional (`fp/`)
  ---------- ------------------- --------------------
  Thiết kế   Class & objects     Pure functions
  Elitism    Có                  Không
  State      Lưu trong objects   Trả về qua tuples
  Test       Mock objects        Test từng hàm
  Mở rộng    Kế thừa classes     Thay đổi functions

Cả hai cho **kết quả tương tự** khi dùng cùng `seed`.

<!-- ------------------------------------------------------------------------

## Ưu điểm & Hạn chế của GA

### Ưu điểm

-   Không cần thông tin gradient\
-   Khám phá song song nhiều nghiệm\
-   Linh hoạt với nhiều bài toán\
-   Reproducible nhờ `seed`\
-   Dễ song song hóa

### Hạn chế

-   Không đảm bảo tối ưu toàn cục\
-   Cần tinh chỉnh tham số\
-   Dễ hội tụ sớm\
-   Chậm hơn thuật toán chuyên dụng -->

------------------------------------------------------------------------
## Yêu cầu môi trường

-   Python `3.13.x`

Cài dependencies:

``` bash
pip install pytest matplotlib
```

------------------------------------------------------------------------
## Chạy chương trình

### Chạy mặc định

``` bash
python oop/run.py
python fp/run.py
```

------------------------------------------------------------------------

### Chạy test

``` bash
python oop/tests/test_onemax.py
python oop/tests/test_knapsack.py

python fp/tests/test_onemax.py
python fp/tests/test_knapsack.py
```

Test có 3 mức: - `small` - `medium` - `large`

Chỉnh trong `SELECTED_LEVELS`.

------------------------------------------------------------------------

## Giải thích output

-   `best_fitness`
-   `best_solution`
-   `history length`
-   `runtime`

Knapsack thêm: - `selected_indices` - `total_weight` - `total_value`

------------------------------------------------------------------------

## Ghi chú

-   Hai phiên bản dùng cùng logic, khác cách tổ chức code\
-   OOP có elitism, FP không\
-   Kết quả tương tự nếu cùng seed


------------------------------------------------------------------------

## Phản ánh và so sánh

  Tiêu chí    FP              OOP
  ----------- --------------- -------------------
  Độ dễ đọc   Cao (hàm nhỏ)   Cao (cấu trúc rõ)
  Mở rộng     Khó             Dễ
  Test        Dễ              Dễ
  Hiệu suất   Tương tự        Tương tự
  Bảo trì     Khó khi lớn     Dễ hơn

FP hợp bài toán nhỏ, OOP hợp hệ thống phức tạp.



