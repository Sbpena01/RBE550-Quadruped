// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from custom_interface:msg/ImuData.idl
// generated code does not contain a copyright notice

#include "custom_interface/msg/detail/imu_data__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_custom_interface
const rosidl_type_hash_t *
custom_interface__msg__ImuData__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x4a, 0x30, 0xaf, 0x6c, 0x67, 0xc5, 0x0c, 0xf7,
      0x04, 0x18, 0x61, 0x06, 0xc6, 0x95, 0xa3, 0x44,
      0xd6, 0x32, 0x21, 0x2a, 0xe3, 0xfb, 0x26, 0x56,
      0xdd, 0xf0, 0xe6, 0x33, 0x86, 0x54, 0x83, 0xa1,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char custom_interface__msg__ImuData__TYPE_NAME[] = "custom_interface/msg/ImuData";

// Define type names, field names, and default values
static char custom_interface__msg__ImuData__FIELD_NAME__roll[] = "roll";
static char custom_interface__msg__ImuData__FIELD_NAME__pitch[] = "pitch";
static char custom_interface__msg__ImuData__FIELD_NAME__yaw[] = "yaw";

static rosidl_runtime_c__type_description__Field custom_interface__msg__ImuData__FIELDS[] = {
  {
    {custom_interface__msg__ImuData__FIELD_NAME__roll, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {custom_interface__msg__ImuData__FIELD_NAME__pitch, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {custom_interface__msg__ImuData__FIELD_NAME__yaw, 3, 3},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
custom_interface__msg__ImuData__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {custom_interface__msg__ImuData__TYPE_NAME, 28, 28},
      {custom_interface__msg__ImuData__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 roll\n"
  "float64 pitch\n"
  "float64 yaw";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
custom_interface__msg__ImuData__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {custom_interface__msg__ImuData__TYPE_NAME, 28, 28},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 38, 38},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
custom_interface__msg__ImuData__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *custom_interface__msg__ImuData__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
