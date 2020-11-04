import numpy as np

rain_wet = np.array([-1.9,-6.9,5.2,5.0,7.3,6.8,0.9,-12.5,1.5,3.8])
rain_air_pressure = np.array([3.2,10.4,2.0,2.5,0.0,12.7,-15.4,-2.5,1.3,6.8])

urain_wet = np.array([0.2,-0.1,0.4,2.7,2.1,-4.6,-1.7,-2.6,2.6,-2.8],dtype=float)
urain_air_pressure = np.array([6.2,7.5,14.6,8.3,0.8,4.3,10.9,13.1,12.8,10.0],dtype=float)

rain_avg = np.array([[rain_wet.mean()],
                    [rain_air_pressure.mean()]])

urain_avg = np.array([[urain_wet.mean()],
                      [urain_air_pressure.mean()]])

avgr_reduce_avgu = rain_avg - urain_avg

rain_cov_ni = np.linalg.inv(np.cov(rain_wet,rain_air_pressure))

rain_temp = np.dot(rain_cov_ni ,avgr_reduce_avgu)

rule = (rain_avg + urain_avg) / 2
print("判别函数为：")
print("w(x) = (x1 - %f  x2 - %f) * %s" %(rule[0], rule[1], rain_temp))
print("判定规则为：")
print("w(x) > 0，是雨天; w(x) < 0，是非雨天")
predicting_data = np.array([[0.6],[3.0]])
result = np.dot(((predicting_data - rule).T), rain_temp)
predict_result = result[0]
if predict_result >= 0:
    print("根据判定结果：明天下雨")
else:
    print("根据判定结果：明天不下雨")
