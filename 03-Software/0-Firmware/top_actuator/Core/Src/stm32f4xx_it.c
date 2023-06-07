/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file    stm32f4xx_it.c
  * @brief   Interrupt Service Routines.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2023 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "stm32f4xx_it.h"
/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN TD */

/* USER CODE END TD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

#define GEAR_RATIO	80
#define DUTY_PERCENTAGE_LIMIT 	0.95

#define ANTI_WIND_UP 	40

#define	BUF_SIZE	8
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
/* USER CODE BEGIN PV */

/* USB related */
extern int16_t move_x;
extern int16_t move_y;

char error_code = 0;
uint8_t external_shutdown = 0;
uint8_t ack_to_be_sent = 0;
uint8_t steady_state_counter = 0;

uint16_t i;
uint16_t led_bool;
uint8_t usb_out[BUF_SIZE] = "Hello\n";
uint8_t blink_led_cmd[BUF_SIZE];
uint8_t usb_in[BUF_SIZE];
uint8_t check_receive;
uint8_t usb_temp[BUF_SIZE];

uint8_t empty_string[BUF_SIZE] = "";
uint8_t acknowledge_message[BUF_SIZE] = "a\n";
uint8_t error_message[BUF_SIZE] = "e\n";

/* Define and initialize the encoder and motor position variables (pulse counters) */
int enc1_pos = 0;
int enc2_pos = 0;

float enc1_pos_cm = 0;
float enc2_pos_cm = 0;

/* Position set */
float mot1_set_pos = 0;
float mot2_set_pos = 0;
float mot1_set_pos_cm = 0;
float mot2_set_pos_cm = 0;

extern float Y_curr;
extern float Y_ref;

/* PID related*/
extern uint32_t PID_freq;

float pos_error1 = 0.0;
float pos_error2 = 0.0;
float pre_pos_error1 = 0.0;
float pre_pos_error2 = 0.0;
float int_error1 = 0.0;
float int_error2 = 0.0;

float kp1 = 10.0;
float ki1 = 5.0;
float kd1 = 0.0;

float kp2 = 10.0;
float ki2 = 5.0;
float kd2 = 0.0;


/* PWM-Specific Variables */
int duty1 = 0;
int duty2 = 0;

/* Define pin state */
GPIO_PinState LOW = 0;
GPIO_PinState HIGH = 1;
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
/* USER CODE BEGIN PFP */
extern uint8_t CDC_Transmit_FS(uint8_t* Buf, uint16_t Len);
extern int8_t CDC_Receive_FS(uint8_t* Buf, uint32_t Len);

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/* External variables --------------------------------------------------------*/
extern PCD_HandleTypeDef hpcd_USB_OTG_FS;
extern TIM_HandleTypeDef htim4;
/* USER CODE BEGIN EV */
extern TIM_HandleTypeDef htim1;
/* USER CODE END EV */

/******************************************************************************/
/*           Cortex-M4 Processor Interruption and Exception Handlers          */
/******************************************************************************/
/**
  * @brief This function handles Non maskable interrupt.
  */
void NMI_Handler(void)
{
  /* USER CODE BEGIN NonMaskableInt_IRQn 0 */

  /* USER CODE END NonMaskableInt_IRQn 0 */
  /* USER CODE BEGIN NonMaskableInt_IRQn 1 */
  while (1)
  {
  }
  /* USER CODE END NonMaskableInt_IRQn 1 */
}

/**
  * @brief This function handles Hard fault interrupt.
  */
void HardFault_Handler(void)
{
  /* USER CODE BEGIN HardFault_IRQn 0 */

  /* USER CODE END HardFault_IRQn 0 */
  while (1)
  {
    /* USER CODE BEGIN W1_HardFault_IRQn 0 */
    /* USER CODE END W1_HardFault_IRQn 0 */
  }
}

/**
  * @brief This function handles Memory management fault.
  */
void MemManage_Handler(void)
{
  /* USER CODE BEGIN MemoryManagement_IRQn 0 */

  /* USER CODE END MemoryManagement_IRQn 0 */
  while (1)
  {
    /* USER CODE BEGIN W1_MemoryManagement_IRQn 0 */
    /* USER CODE END W1_MemoryManagement_IRQn 0 */
  }
}

/**
  * @brief This function handles Pre-fetch fault, memory access fault.
  */
void BusFault_Handler(void)
{
  /* USER CODE BEGIN BusFault_IRQn 0 */

  /* USER CODE END BusFault_IRQn 0 */
  while (1)
  {
    /* USER CODE BEGIN W1_BusFault_IRQn 0 */
    /* USER CODE END W1_BusFault_IRQn 0 */
  }
}

/**
  * @brief This function handles Undefined instruction or illegal state.
  */
void UsageFault_Handler(void)
{
  /* USER CODE BEGIN UsageFault_IRQn 0 */

  /* USER CODE END UsageFault_IRQn 0 */
  while (1)
  {
    /* USER CODE BEGIN W1_UsageFault_IRQn 0 */
    /* USER CODE END W1_UsageFault_IRQn 0 */
  }
}

/**
  * @brief This function handles System service call via SWI instruction.
  */
void SVC_Handler(void)
{
  /* USER CODE BEGIN SVCall_IRQn 0 */

  /* USER CODE END SVCall_IRQn 0 */
  /* USER CODE BEGIN SVCall_IRQn 1 */

  /* USER CODE END SVCall_IRQn 1 */
}

/**
  * @brief This function handles Debug monitor.
  */
void DebugMon_Handler(void)
{
  /* USER CODE BEGIN DebugMonitor_IRQn 0 */

  /* USER CODE END DebugMonitor_IRQn 0 */
  /* USER CODE BEGIN DebugMonitor_IRQn 1 */

  /* USER CODE END DebugMonitor_IRQn 1 */
}

/**
  * @brief This function handles Pendable request for system service.
  */
void PendSV_Handler(void)
{
  /* USER CODE BEGIN PendSV_IRQn 0 */

  /* USER CODE END PendSV_IRQn 0 */
  /* USER CODE BEGIN PendSV_IRQn 1 */

  /* USER CODE END PendSV_IRQn 1 */
}

/**
  * @brief This function handles System tick timer.
  */
void SysTick_Handler(void)
{
  /* USER CODE BEGIN SysTick_IRQn 0 */

  /* USER CODE END SysTick_IRQn 0 */
  HAL_IncTick();
  /* USER CODE BEGIN SysTick_IRQn 1 */

  /* USER CODE END SysTick_IRQn 1 */
}

/******************************************************************************/
/* STM32F4xx Peripheral Interrupt Handlers                                    */
/* Add here the Interrupt Handlers for the used peripherals.                  */
/* For the available peripheral interrupt handler names,                      */
/* please refer to the startup file (startup_stm32f4xx.s).                    */
/******************************************************************************/

/**
  * @brief This function handles EXTI line0 interrupt.
  */
void EXTI0_IRQHandler(void)
{
  /* USER CODE BEGIN EXTI0_IRQn 0 */
	/* Check rising of falling*/
	if (HAL_GPIO_ReadPin(GPIOA, ENC1_A_Pin)){
		/* high means the interrupt was rising */
		if (HAL_GPIO_ReadPin(GPIOA, ENC1_B_Pin)){
			/* Update the position of the first motor */
			enc1_pos ++;
			}else{
			enc1_pos --;
		}
	}
	if (!HAL_GPIO_ReadPin(GPIOA, ENC1_A_Pin)){
		/* low means the interrupt was falling */
		if (HAL_GPIO_ReadPin(GPIOA, ENC1_B_Pin)){
			/* Update the position of the first motor */
			enc1_pos --;
			}else{
			enc1_pos ++;
		}
	}
	enc1_pos_cm = (float)enc1_pos/(float)(GEAR_RATIO);
  /* USER CODE END EXTI0_IRQn 0 */
  HAL_GPIO_EXTI_IRQHandler(ENC1_A_Pin);
  /* USER CODE BEGIN EXTI0_IRQn 1 */

  /* USER CODE END EXTI0_IRQn 1 */
}

/**
  * @brief This function handles EXTI line2 interrupt.
  */
void EXTI2_IRQHandler(void)
{
  /* USER CODE BEGIN EXTI2_IRQn 0 */
	/* Check rising of falling*/
	if (HAL_GPIO_ReadPin(GPIOA, ENC2_A_Pin)){
		/* high means the interrupt was rising */
		if (HAL_GPIO_ReadPin(GPIOA, ENC2_B_Pin)){
			/* Update the position of the first motor */
			enc2_pos ++;
			}else{
			enc2_pos --;
		}
	}
	if (!HAL_GPIO_ReadPin(GPIOA, ENC2_A_Pin)){
		/* low means the interrupt was falling */
		if (HAL_GPIO_ReadPin(GPIOA, ENC2_B_Pin)){
			/* Update the position of the first motor */
			enc2_pos --;
			}else{
			enc2_pos ++;
		}
	}
	enc2_pos_cm = (float)enc2_pos/(float)(GEAR_RATIO);
  /* USER CODE END EXTI2_IRQn 0 */
  HAL_GPIO_EXTI_IRQHandler(ENC2_A_Pin);
  /* USER CODE BEGIN EXTI2_IRQn 1 */

  /* USER CODE END EXTI2_IRQn 1 */
}

/**
  * @brief This function handles TIM4 global interrupt.
  */
void TIM4_IRQHandler(void)
{
  /* USER CODE BEGIN TIM4_IRQn 0 */

	if(error_code == 0 && external_shutdown == 0){

		/* Determine set values (NO INVERSE KINEMATICS) */
		mot1_set_pos_cm = Y_ref;
		mot2_set_pos_cm = Y_ref;
		mot1_set_pos = (int)(mot1_set_pos_cm*GEAR_RATIO);
		mot2_set_pos = (int)(mot2_set_pos_cm*GEAR_RATIO);

		/* Determine PID errors */
		pos_error1 = mot1_set_pos - enc2_pos;
		pos_error2 = mot2_set_pos - enc1_pos;

		float der_error1=(pos_error1-pre_pos_error1)*PID_freq;
		float der_error2=(pos_error2-pre_pos_error2)*PID_freq;

		int_error1+=pos_error1/PID_freq;
		int_error2+=pos_error2/PID_freq;

		if (int_error1>=ANTI_WIND_UP) int_error1=ANTI_WIND_UP;
		if (int_error2>=ANTI_WIND_UP) int_error2=ANTI_WIND_UP;

		if (int_error1<=-ANTI_WIND_UP) int_error1=-ANTI_WIND_UP;
		if (int_error2<=-ANTI_WIND_UP) int_error2=-ANTI_WIND_UP;

		if (((pos_error1>0) && (int_error1<0))||((pos_error1<0) && (int_error1>0))) int_error1=0;
		if (((pos_error2>0) && (int_error2<0))||((pos_error2<0) && (int_error2>0))) int_error2=0;

		pre_pos_error1=pos_error1;
		pre_pos_error2=pos_error2;

		/* Set the duty (only proportional implemented for now) */
		duty1 = (int)(kp1*pos_error1+kd1*der_error1+ki1*int_error1);
		duty2 = (int)(kp2*pos_error2+kd2*der_error2+ki2*int_error2);

		/* Set the direction */
		if(duty1 > 0){
				HAL_GPIO_WritePin(GPIOB, IN1_A_Pin, HIGH);
				HAL_GPIO_WritePin(GPIOB, IN1_B_Pin, LOW);
		}
		else{
				duty1 = -duty1;
				HAL_GPIO_WritePin(GPIOB, IN1_B_Pin, HIGH);
				HAL_GPIO_WritePin(GPIOB, IN1_A_Pin, LOW);
		}
		if(duty2 > 0){
				HAL_GPIO_WritePin(GPIOB, IN2_A_Pin, HIGH);
				HAL_GPIO_WritePin(GPIOB, IN2_B_Pin, LOW);
		}
		else{
				duty2 = -duty2;
				HAL_GPIO_WritePin(GPIOB, IN2_B_Pin, HIGH);
				HAL_GPIO_WritePin(GPIOB, IN2_A_Pin, LOW);
		}

		/* Limit the duty */
		if(duty1 > ((htim1.Init.Period+1)*DUTY_PERCENTAGE_LIMIT)){
				duty1 = (htim1.Init.Period+1)*DUTY_PERCENTAGE_LIMIT;
			}
		if(duty2 > ((htim1.Init.Period+1)*DUTY_PERCENTAGE_LIMIT)){
				duty2 = (htim1.Init.Period+1)*DUTY_PERCENTAGE_LIMIT;
			}

		// Set the duty values to zero if steady state is reached
		if ((fabs(pos_error1) <= 5) && (fabs(pos_error2) <= 5)){
			TIM1->CCR1 = 0;
			TIM1->CCR2 = 0;
			if(ack_to_be_sent == 1){
				memcpy(&usb_out, &acknowledge_message, sizeof(usb_out));
				CDC_Transmit_FS(usb_out, sizeof(usb_out));
				ack_to_be_sent = 0;
			}
		}
		else {
			TIM1->CCR1 = duty1;
			TIM1->CCR2 = duty2;
		}

	}
	else{
		TIM1->CCR1 = 0;
		TIM1->CCR2 = 0;
		memcpy(&usb_out, &error_message, sizeof(usb_out));
		CDC_Transmit_FS(usb_out, sizeof(usb_out));
	}

	Y_curr = (enc1_pos_cm + enc2_pos_cm)/2;
  /* USER CODE END TIM4_IRQn 0 */
  HAL_TIM_IRQHandler(&htim4);
  /* USER CODE BEGIN TIM4_IRQn 1 */

  /* USER CODE END TIM4_IRQn 1 */
}

/**
  * @brief This function handles USB On The Go FS global interrupt.
  */
void OTG_FS_IRQHandler(void)
{
  /* USER CODE BEGIN OTG_FS_IRQn 0 */

	CDC_Receive_FS(usb_temp,sizeof(usb_temp));

	if(strcmp((char *)usb_temp, (char *)empty_string) != 0){
		HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);

		// Store the data in usb_in array if a non-empty message received
		memcpy(&usb_in, &usb_temp, sizeof(usb_in));

		/* Parsing USB Message*/
		if(usb_in[0] == 'm'){
			// Since STM32 byte size is 16 bits, there isn't a real uint8_t type
			// We manually do big endian storage, and manually decode them below here
			move_x = usb_in[1]*256 + usb_in[2];
			move_y = usb_in[3]*256 + usb_in[4];

			/* FOR DEBUGGING PURPOSES
			usb_in[1] = move_x/256;
			usb_in[2] = move_x%256;
			usb_in[3] = move_y/256;
			usb_in[4] = move_y%256;
			usb_in[5] = '\n';
			CDC_Transmit_FS(usb_in,sizeof(usb_in));
			*/

			Y_ref = Y_ref + (float)move_y/10;

			ack_to_be_sent = 1;

		}

		if(usb_in[0] == 's'){
			external_shutdown = 1;
		}

		if(usb_in[0] == 'i'){
			// Since STM32 byte size is 16 bits, there isn't a real uint8_t type
			// We manually do big endian storage, and manually decode them below here
			/*
			int16_t mot_inner_move = usb_in[1]*256 + usb_in[2];
			int16_t mot_middle_move = usb_in[3]*256 + usb_in[4];
			int16_t mot_outer_move = usb_in[5]*256 + usb_in[6];

			if(mot_inner_move < 5){
				mot1_set_pos = mot1_set_pos + mot_inner_move;
			}
			if(mot_middle_move < 5){
				mot2_set_pos = mot2_set_pos + mot_middle_move;
			}
			if(mot_outer_move < 5){
				mot_outer_set_pos = mot_outer_set_pos + mot_outer_move;
			}
			*/
		}

		if(usb_in[0] == 'o'){
			// TURN OFF CODE TO BE ADDED
		}

		if(usb_in[0] == 'b'){
			// BEGIN COMMAND
		}

	}

	// Clear usb_temp array
	memset(usb_temp, 0, sizeof(usb_temp));

  /* USER CODE END OTG_FS_IRQn 0 */
  HAL_PCD_IRQHandler(&hpcd_USB_OTG_FS);
  /* USER CODE BEGIN OTG_FS_IRQn 1 */

  /* USER CODE END OTG_FS_IRQn 1 */
}

/* USER CODE BEGIN 1 */

/* USER CODE END 1 */
