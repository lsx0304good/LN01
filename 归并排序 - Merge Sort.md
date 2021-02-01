## 归并排序 - Merge Sort

### Python 实现

```python
def merge(s1, s2, s):
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] <= s2[j]:
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s2[j]
            j += 1

    while i < len(s1):
        s[i + j] = s1[i]
        i += 1

    while j < len(s2):
        s[i + j] = s2[j]
        j += 1


def merge_sort(s):
    n = len(s)
    if n < 2:
        return
    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]
    merge_sort(s1)
    merge_sort(s2)
    merge(s1, s2, s)
```

## 

### Java 实现

```java
import java.util.Arrays;
public class merge_sort {
    public static void main(String[] args) {
        int[] arr1 = new int[] {1,6,8,2,2,4,6,10,5,9,7};
        mergeSort(arr1);
        System.out.println(Arrays.toString(arr1));

    }

    public static void mergeSort(int[] array) {
        if (array == null || array.length < 2) {
            return;
        }
        process(array, 0, array.length - 1);
    }

    public static void process (int[] arr, int L, int R) {
        if (L == R) {
            return;
        }
        int mid = L + ((R - L) >> 1);  // 右位移，防止整型溢出，实际效果等于除以2
        process(arr, L, mid);
        process(arr, mid + 1, R);
        merge(arr, L, mid, R);
    }

    public static void merge(int[] arr, int L, int M, int R) {
        int[] help = new int[R - L + 1];  // 建立新数组来记录整理后的数组
        int i = 0;
        int p1 = L;
        int p2 = M + 1;

        while (p1 <= M && p2 <= R) {
            help[i++] = arr[p1] <= arr[p2] ? arr[p1++] : arr[p2++];
        }

        while (p1 <= M) {
            help[i++] = arr[p1++];
        }

        while (p2 <= R) {
            help[i++] = arr[p2++];
        }

        for (i = 0; i < help.length; i ++) {
            arr[L + i] = help[i];
        }


    }
}
```