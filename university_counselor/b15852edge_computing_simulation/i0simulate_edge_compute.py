import time
import timeit
import random
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

from i3reforcelearning_experiment import Load_mapping_experiment


def heat_heavy_function(dummy_input: int):
    print('heat_heavy_function', dummy_input)
    """mimic IO/Heat heavy task (e.g. download webpage) using time.sleep"""
    tot = random.randint(0, 1000)
    tot = random.randint(0, 100)
    time.sleep(0.001)
    return tot % 10


def cpu_timecounsume_function(dummy_input: int):
    print('cpu_timecounsume_function', dummy_input)
    """mimic CPU heavy task (e.g. scientific calculation) using random.randint"""
    # tot = sum([random.randint(0, 10) for i in range(110000)])
    # tot = sum([random.randint(0, 10) for i in range(11000)])

    tot = sum([random.randint(0, 10) for i in range(200)])
    return tot % 10


def eval_parallel(parallel_method: str, function_type: str, n_workers: int):
    """evaluate multi-thread or multi-process performance"""
    # whether use multi thread or multi process
    parallel_method_dict = {
        "multithread": ThreadPoolExecutor,
        "multiprocess": ProcessPoolExecutor,
    }
    # whether the function is io-heavy or cpu-heavy
    function_type_dict = {
        "heat_heavy": heat_heavy_function,
        "cpu_timecounsume": cpu_timecounsume_function,
    }
    the_method = parallel_method_dict[parallel_method]
    the_function = function_type_dict[function_type]

    # 运行该函数 10 次（~10 秒），并使用 n_workers 并行
    n_item = 10
    with the_method(n_workers) as executor:
        results = executor.map(the_function, range(n_item))
    return sum([x for x in results])


def main():
    # 启动所有并行计算方法和函数类型
    method_function_list = [
        ("multithread", "heat_heavy"),
        ("multithread", "cpu_timecounsume"),
        ("multiprocess", "heat_heavy"),
        ("multiprocess", "cpu_timecounsume"),
    ]

    # 计算 eval 并行的次数以提供准确的度量
    n_eval = 5
    n_worker_list = range(1, 5)
    result_df_list = []

    # 依次运行给定的并行方法和函数
    for the_method, the_function in method_function_list:
        time_list = [
            timeit.timeit(
                'eval_parallel("{0}", "{1}", {2})'.format(
                    the_method, the_function, n_worker
                ),
                number=n_eval,
                globals=globals(),
            )
            / n_eval
            for n_worker in n_worker_list
        ]
        print(" -- completed evalulate: {0}, {1} -- ".format(the_method, the_function))
        result_df_list.append(
            pd.DataFrame(
                {
                    "method": the_method,
                    "function": the_function,
                    "n_workers": n_worker_list,
                    "time_spent": time_list,
                }
            )
        )
    result_df = pd.concat(result_df_list)
    print(result_df)
    Load_mapping_experiment(result_df, 'heat_heavy')
    Load_mapping_experiment(result_df, 'cpu_timecounsume')


if __name__ == "__main__":
    main()

'''
heat
启发式算法模拟
gamma= 0.8766839326725466
2021-12-22 01:03:22.623 Python[25136:1730071] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to (null)
平均回合奖励 = 762 / 100 = 7.62
-------------------- step 4
QLearning算法模拟
gamma= 0.9266839326725467
平均回合奖励 = 821 / 100 = 8.21


timeconsume
启发式算法模拟
gamma= 0.8734955448752378
平均回合奖励 = 778 / 100 = 7.78
-------------------- step 4
QLearning算法模拟
gamma= 0.9234955448752378
平均回合奖励 = 851 / 100 = 8.51

'''
