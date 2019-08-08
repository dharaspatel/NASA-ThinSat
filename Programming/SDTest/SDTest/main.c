/*
 * GccApplication1.c
 *
 * Created: 2019-08-07 16:09:05
 * Author : Justin Kunimune
 */ 
#include <string.h>
#include "fat.h"
#include "fat_config.h"
#include "partition.h"
#include "sd_raw.h"
#include "sd_raw_config.h"


uint8_t find_file_in_dir(struct fat_fs_struct* fs, struct fat_dir_struct* dd, const char* name, struct fat_dir_entry_struct* dir_entry)
{
	while(fat_read_dir(dd, dir_entry))
	{
		if(strcmp(dir_entry->long_name, name) == 0)
		{
			fat_reset_dir(dd);
			return 1;
		}
	}

	return 0;
}

struct fat_file_struct* open_file_in_dir(struct fat_fs_struct* fs, struct fat_dir_struct* dd, const char* name)
{
	struct fat_dir_entry_struct file_entry;
	if(!find_file_in_dir(fs, dd, name, &file_entry))
	return 0;

	return fat_open_file(fs, &file_entry);
}


int main() {
  /* setup sd card slot */
  sd_raw_init();

  /* open first partition */
  struct partition_struct* partition = partition_open(sd_raw_read, sd_raw_read_interval, 0, 0, 0);

  if(!partition)
  {
	/* If the partition did not open, assume the storage device
		* is a "superfloppy", i.e. has no MBR.
		*/
    partition = partition_open(sd_raw_read, sd_raw_read_interval, 0, 0, -1);
  }

  /* open file system */
  struct fat_fs_struct* fs = fat_open(partition);

  /* open root directory */
  struct fat_dir_entry_struct directory;
  fat_get_dir_entry_of_path(fs, "/", &directory);

  struct fat_dir_struct* dd = fat_open_dir(fs, &directory);
  struct fat_file_struct* fd = open_file_in_dir(fs, dd, "forecast_d00.dat");

  uint8_t buffer[8];
  uint32_t offset = 0;
  intptr_t count;
  while((count = fat_read_file(fd, buffer, sizeof(buffer))) > 0)
  {
    /* do something with the data in buffer here */
	offset += sizeof(buffer);
  }

  fat_close_file(fd);
  
  /* close directory */
  fat_close_dir(dd);

  /* close file system */
  fat_close(fs);

  /* close partition */
  partition_close(partition);
}
