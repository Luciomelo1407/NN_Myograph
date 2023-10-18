#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

void maximum (uint16_t *array, int size, int mask_size, uint16_t *result);
void minimum (uint16_t *array, int size, int mask_size, uint16_t *result);
void median (uint16_t *array, int size, int mask_size, uint16_t *result);
void sort (uint16_t *array, int mask_size);

void sort (uint16_t *array, int mask_size)
{
  for (int i = 0; i < mask_size; i++)
  {
    int min = array[i];
    for (int j = i; j < mask_size; j++)
    {
      if (array[j] < min)
      {
        min = array[j];
      }
    }
  }
}

void maximum (uint16_t *array, int size, int mask_size, uint16_t *result)
{
  uint16_t *mask = (uint16_t *) calloc(mask_size, sizeof(uint16_t));
  int median = mask_size / 2;
  for (int i = median; i < size - median; i++)
  {
    for (int j = -median; j < median; j++)
    {
      mask[median + j] = array[i];
    }
    sort(mask, mask_size);
    result[i] = mask[mask_size - 1];
  }
  free(mask);
}

void minimum (uint16_t *array, int size, int mask_size, uint16_t *result)
{
  uint16_t *mask = (uint16_t *) calloc(mask_size, sizeof(uint16_t));
  int median = mask_size / 2;
  for (int i = median; i < size - median; i++)
  {
    for (int j = -median; j < median; j++)
    {
      mask[median + j] = array[i];
    }
    sort(mask, mask_size);
    result[i] = mask[0];
  }
  free(mask);
}

void median (uint16_t *array, int size, int mask_size, uint16_t *result)
{
  uint16_t *mask = (uint16_t *) calloc(mask_size, sizeof(uint16_t));
  int median = mask_size / 2;
  for (int i = median; i < size - median; i++)
  {
    for (int j = -median; j < median; j++)
    {
      mask[median + j] = array[i];
    }
    sort(mask, mask_size);
    result[i] = mask[median];
  }
  free(mask);
}
