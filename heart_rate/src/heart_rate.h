#ifndef _HEART_RATE_H_
#define _HEART_RATE_H_

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define FIAR_PARAM      6
#define FILT_AV_SIZE    32 //change also in heartrate.h
#define LOG_2_FILT_AV   5

struct HR_algo_state {
    uint8_t maybe_peak;
    uint8_t maybe_valley;
    uint8_t peak_detect;
    uint8_t valley_detect;
    uint8_t fiar;               //stands for five-in-a-row
    int32_t valley_min;
    int32_t peak_max;
    uint8_t offset_DC;
    uint8_t offset_filt;
    int32_t xbuf_DC[32];        //FILT_AV
    int32_t abuf_DC[32];
    int32_t cbuf[32];
    int32_t lastSample;
    int32_t artifact_cnt;
};

void heart_rate_init (void);
int32_t heart_rate_process(int32_t LED_data_vector);
int32_t check_for_beat(int32_t *output_buffer, int32_t *avg_estimate, int32_t sample, struct HR_algo_state* HR_state);
int HR_sleep(void);
int HR_wake_up(void);

#endif